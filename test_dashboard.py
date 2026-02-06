#!/usr/bin/env python3
"""Generate a test dashboard with mock data."""

from datetime import datetime, timedelta
from jinja2 import Environment, FileSystemLoader
import pytz

# Create mock workflow data
class MockWorkflow:
    def __init__(self, name, status, hours_ago):
        self.workflow_name = f"{name}.yml"
        self.lf_workflow_name = name
        self.workflow_url = f"https://github.com/example/repo/actions/workflows/{name}.yml"
        self.workflow_status = status
        self.is_stale = hours_ago > 48
        
        if status == "success":
            self.display_class = "green-cell"
            self.icon_class = "fa fa-check-circle"
        elif status == "failure":
            self.display_class = "red-cell"
            self.icon_class = "fa fa-times-circle"
        else:
            self.display_class = "yellow-cell"
            self.icon_class = "fa fa-question-circle"
        
        conclusion_dt = datetime.now() - timedelta(hours=hours_ago)
        self.conclusion_time = conclusion_dt.strftime("%m/%d %H:%M")

class MockProject:
    def __init__(self, owner, repo, workflows):
        self.owner = owner
        self.repo = repo
        self.repo_url = f"https://github.com/{owner}/{repo}"
        self.other_workflows = workflows

# Create example projects
projects = [
    MockProject("org", "project-a", [
        MockWorkflow("ci", "success", 2),
        MockWorkflow("build", "success", 3),
    ]),
    MockProject("org", "project-b", [
        MockWorkflow("test", "failure", 1),
        MockWorkflow("deploy", "success", 4),
    ]),
    MockProject("org", "project-c", [
        MockWorkflow("lint", "success", 5),
        MockWorkflow("security", "pending", 12),
        MockWorkflow("docs", "success", 24),
    ]),
]

timezone = pytz.timezone("America/New_York")
last_updated = datetime.now(timezone).strftime("%H:%M %B %d, %Y (US-NYC)")

context = {
    "page_title": "Test GitHub Actions Dashboard",
    "all_projects": projects,
    "dash_name": "Test Dashboard",
    "dash_repo": "cf-gha-dash",
    "last_updated": last_updated,
}

environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("dash_template.jinja")

with open("html/test_dashboard.html", mode="w", encoding="utf-8") as f:
    f.write(template.render(context))

print("✅ Test dashboard generated at html/test_dashboard.html")
