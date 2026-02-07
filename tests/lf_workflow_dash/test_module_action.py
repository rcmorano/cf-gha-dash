import os

import pytest

from lf_workflow_dash.data_types import read_yaml_file
from lf_workflow_dash.update_dashboard import update_html


@pytest.mark.parametrize(
    "datafile, outfile",
    [
        # Only testing tracked_workflows.yaml as other config files don't exist in this fork
        ("config/tracked_workflows.yaml", "lincc_output.html"),
    ],
)
def test_do_the_work(datafile, outfile, tmp_path):
    output_path = os.path.join(tmp_path, outfile)
    context = read_yaml_file(datafile)
    update_html(output_path, context)


def test_workflows_key_compatibility(tmp_path):
    """Test that both 'workflows' and 'other-workflows' keys work correctly."""
    # Test with new 'workflows' key
    yaml_content = """
page_title: test-dash
repos:
  - repo: test-repo
    owner: test-owner
    workflows:
      test-workflow: test.yml
      build: build.yml
"""
    yaml_path = os.path.join(tmp_path, "test_workflows.yaml")
    with open(yaml_path, "w") as f:
        f.write(yaml_content)

    context = read_yaml_file(yaml_path)
    assert len(context["all_projects"]) == 1
    project = context["all_projects"][0]
    assert len(project.workflows) == 2
    assert project.workflows[0].lf_workflow_name in ["test-workflow", "build"]
    assert project.workflows[0].workflow_name in ["test.yml", "build.yml"]
    assert not project.fetch_all_workflows

    # Test with old 'other-workflows' key (backwards compatibility)
    yaml_content = """
page_title: test-dash
repos:
  - repo: test-repo
    owner: test-owner
    other-workflows:
      test-workflow: test.yml
      build: build.yml
"""
    yaml_path = os.path.join(tmp_path, "test_other_workflows.yaml")
    with open(yaml_path, "w") as f:
        f.write(yaml_content)

    context = read_yaml_file(yaml_path)
    assert len(context["all_projects"]) == 1
    project = context["all_projects"][0]
    assert len(project.workflows) == 2
    assert project.workflows[0].lf_workflow_name in ["test-workflow", "build"]
    assert not project.fetch_all_workflows


def test_workflows_all_value(tmp_path):
    """Test that workflows: 'all' sets the fetch_all_workflows flag."""
    yaml_content = """
page_title: test-dash
repos:
  - repo: test-repo
    owner: test-owner
    workflows: all
"""
    yaml_path = os.path.join(tmp_path, "test_all_workflows.yaml")
    with open(yaml_path, "w") as f:
        f.write(yaml_content)

    context = read_yaml_file(yaml_path)
    assert len(context["all_projects"]) == 1
    project = context["all_projects"][0]
    assert project.fetch_all_workflows
    assert len(project.workflows) == 0  # Should be empty until fetch_all_workflows is processed
