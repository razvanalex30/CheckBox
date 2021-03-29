import time

from selenium import webdriver
# from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from driver_create import SeleniumLibraryExt

class CheckBox:

    def __init__(self):
        self.menu = None
    
    def find_checkboxes(self):
        self.driver = SeleniumLibraryExt.create_driver()
        self.driver.find_element_by_xpath("//button[@aria-label='Expand all']").click()
        menus = list()
        web_elements = self.driver.find_elements_by_xpath("//span[@class='rct-title']")
        for elem in web_elements:
            menus.append(elem.text)
        self.menu = menus

    def check_selected(self, selection_list):
        self.driver = SeleniumLibraryExt.create_driver()
        for elem in selection_list:
            if elem in self.menu:
                clickable = self.driver.find_element_by_xpath(f"//span[@class='rct-title'][text()='{elem}']")
                self.driver.execute_script("arguments[0].scrollIntoView()", clickable)
                time.sleep(0.5)
                clickable.click()