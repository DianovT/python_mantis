import time

from model.project import Project


def test_create_new_project(app):
    new_project = Project(name=app.gen.random_string('progect', 7))
    old_list_project = app.project.get_list_project()
    app.project.create(new_project)
    time.sleep(3)
    new_list_project = app.project.get_list_project()
    assert len(old_list_project) + 1 == len(new_list_project)
    old_list_project.append(new_project)
    assert sorted(old_list_project, key=Project.name) == sorted(new_list_project, key=Project.name)