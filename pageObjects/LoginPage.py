import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_id = "//*[@id='Email']"
    textbox_password_id = "//*[@id='Password']"
    button_login_xpath = "//*[@type='submit' and text() ='Log in']"
    link_logout_linktext = "Logout"
    slider_bar_xapth = "//*[@class='sidebar-mini layout-fixed control-sidebar-slide-open sidebar-closed sidebar-collapse']"
    main_logo = "//*[@class='nav-icon fas fa-book']/following-sibling::p"


    def __init__(self, driver):
        self.driver = driver

    def user_login(self, username, password):
        # self.driver.find_element_by_xpath(self.textbox_username_id).click()
        self.driver.find_element(By.XPATH, self.textbox_username_id).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_id).send_keys(username)
        self.driver.find_element(By.XPATH, self.textbox_password_id).clear()
        self.driver.find_element(By.XPATH
                                 , self.textbox_password_id).send_keys(password)

        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def Logout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()

    def image_main_logo(self):
        logo = self.driver.find_element(By.XPATH, self.main_logo)
        move = ActionChains(self.driver)
        # move.move_to_element(slider).perform()
        # move.click_and_hold(slider).move_by_offset(100, 0).release().perform()
        move.move_to_element(logo).click().perform()


