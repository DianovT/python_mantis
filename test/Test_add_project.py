import time

from model.project import Project


def test_create_new_project(app):
    new_project = Project(name=app.gen.random_string('project', 7))
    #old_list_project = app.project.get_list_project()
    old_list_project = app.soap.get_projects_list_administrator()
    app.project.create(new_project)
    time.sleep(3)
    #new_list_project = app.project.get_list_project()
    new_list_project = app.soap.get_projects_list_administrator()
    assert len(old_list_project) + 1 == len(new_list_project)
    old_list_project.append(new_project)
    assert sorted(new_list_project, key=Project.id_or_max) == sorted(app.soap.get_projects_list_administrator(),
                                                                     key=Project.id_or_max)