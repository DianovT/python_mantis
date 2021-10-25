from selenium.webdriver.support.ui import Select
from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_manage_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()

    def open_manage_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage Projects").click()

    def attributes_project(self, project):
        wd = self.app.wd
        self.change_field("name", project.name)
        self.change_field("status", project.status)
        self.change_field("view_state", project.view_state)
        self.change_field("description", project.description)

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            if field_name in ('status', 'view_state'):
                wd.find_element_by_name(field_name).click()
                Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
            else:
                wd.find_element_by_name(field_name).click()
                wd.find_element_by_name(field_name).clear()
                wd.find_element_by_name(field_name).send_keys(text)

    def create(self, project):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_manage_page()
        self.open_manage_projects_page()
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        self.attributes_project(project)
        wd.find_element_by_css_selector("input.button").click()
        self.project_cash = None

    def delete_project_by_name(self, project):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_manage_page()
        self.open_manage_projects_page()
        wd.find_element_by_xpath("//a[contains(text(),'" + project + "')]").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_css_selector("input.button").click()
        self.project_cash = None

    project_cash = None

    def get_list_project(self):
        if self.project_cash is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.open_manage_page()
            self.open_manage_projects_page()
            self.project_cash = []
            for element in (wd.find_elements_by_xpath("/html/body/table[3]/tbody/tr")):
                if element.get_attribute("class") not in ('', 'row-category'):
                    cells = element.find_elements_by_tag_name("td")
                    name = cells[0].text
                    self.project_cash.append(Project(name=name))
        return list(filter(None, self.project_cash))