from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from generator.project import GeneratorProject
from webdriver_manager.firefox import GeckoDriverManager


class Application:
    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unknown browser %s" % browser)
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.gen = GeneratorProject(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        # home page
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()