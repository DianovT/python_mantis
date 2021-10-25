from model.project import Project
import random
import time


def test_del_some_project(app):
    if len(app.project.get_list_project()) == 0:
        app.project.create(Project(name=app.gen.random_string('project', 7)))
        time.sleep(3)
    old_list_project = app.project.get_list_project()
    project = random.choice(old_list_project)
    app.project.delete_project_by_name(project.name)
    new_list_project = app.project.get_list_project()
    assert len(old_list_project) - 1 == len(new_list_project)
    old_list_project.remove(project)
    assert old_list_project == new_list_project