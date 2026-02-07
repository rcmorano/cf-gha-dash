from jinja2 import Environment, FileSystemLoader

from lf_workflow_dash.data_types import WorkflowElemData, read_yaml_file
from lf_workflow_dash.github_request import fetch_all_workflows, update_copier_version, update_workflow_status


def update_html(out_file, context):
    """Fetch the jinja template, and update with all of the gathered context.

    Args:
        out_file (str): path to write the hydrated html file to
        context (dict): local variables representing workflow status
    """
    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template("dash_template.jinja")
    with open(out_file, mode="w", encoding="utf-8") as results:
        results.write(template.render(context))


def update_status(context, token):
    """Issue requests to the github JSON API and update each workflow status accordingly.

    Args:
        context (dict): local variables representing workflow status
        token (str): github personal access token
    """
    for project in context["all_projects"]:
        print(project.repo)
        update_copier_version(project, token)

        # If fetch_all_workflows is True, fetch all workflows from the repository
        if project.fetch_all_workflows:
            print("  Fetching all workflows from repository...")
            workflow_files = fetch_all_workflows(project.owner, project.repo, token)
            for workflow_file in workflow_files:
                # Create a WorkflowElemData for each workflow file
                # Use the filename (without extension) as the display name
                workflow_name = workflow_file.replace(".yml", "").replace(".yaml", "")
                project.workflows.append(
                    WorkflowElemData(
                        workflow_file,
                        repo_url=project.repo_url,
                        owner=project.owner,
                        repo=project.repo,
                        lf_workflow_name=workflow_name,
                    )
                )

        update_workflow_status(project.smoke_test, token)
        update_workflow_status(project.build_docs, token)
        update_workflow_status(project.benchmarks, token)
        update_workflow_status(project.live_build, token)
        for workflow in project.workflows:
            update_workflow_status(workflow, token)


def do_the_work(token, datafile, outfile):
    """Wrapper to call all of the methods necessary to build the final hydrated page.

    Args:
        token (str): github personal access token
        datafile (str): path to the yaml config file with workflow data
        outfile (str): write to write the hyrated html file to
    """
    context = read_yaml_file(datafile)
    update_status(context, token)
    update_html(outfile, context)
