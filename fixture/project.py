from selenium.webdriver.support.ui import Select

class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_manage_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def open_add_project_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def open_create_project_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()

    def fill_in_project(self, project):
        wd = self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_name("status").click()
        Select(wd.find_element_by_name("status")).select_by_visible_text(project.status)
        wd.find_element_by_name("view_state").click()
        Select(wd.find_element_by_name("view_state")).select_by_visible_text(project.view_state)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.description)

    def open_delete_project_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()

    def create_new_project(self, project):
        self.open_manage_project_page()
        self.open_create_project_page()
        self.fill_in_project(project)
        self.open_add_project_page()

    def delete_project_by_name(self, name):
        wd = self.app.wd
        self.open_manage_project_page()
        wd.find_element_by_link_text(name).click()
        self.open_delete_project_page()
        self.open_delete_project_page()