from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.action_chains import ActionChains
import time
import pytest


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    # def test_homePageTitle(self, setup):
    #     # breakpoint()
    #     self.logger.info("*****************Test_001_Login*******************")
    #     self.logger.info("*****************Verifing Home Page Title*****************")
    #     self.driver = setup
    #     self.driver.get(self.baseUrl)
    #     act_title = self.driver.title
    #     if act_title == "Your store. Login":
    #         assert True
    #         self.driver.close()
    #         self.logger.info("****************Home Page title test is passed*******************")
    #     else:
    #         self.driver.save_screenshot(".//Screenshots//" + "test_homePageTitle.png")
    #         self.driver.close()
    #         self.logger.info("****************Home Page title test is failed*******************")
    #         assert False
    #
    # def test_login(self, setup):
    #     self.logger.info("***************Verifying Login testing*******************")
    #     self.driver = setup
    #     self.driver.get(self.baseUrl)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.user_login(self.username, self.password)
    #     act_title = self.driver.title
    #
    #     if act_title == "Dashboard / nopCommerce administration":
    #         assert True
    #         self.driver.close()
    #         self.logger.info("***************test login page passed*******************")
    #     else:
    #         self.driver.save_screenshot(".//Screenshots//" + "test_login.png")
    #         self.driver.close()
    #         self.logger.info("***************test login failed*******************")
    #         assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_slider(self, setup):
        self.logger.info("***************Verifying Slider testing*******************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.user_login(self.username, self.password)
        try:
            self.lp.image_main_logo()
            time.sleep(5)
            self.driver.execute_script("window.scrollBy(0,500)")
            time.sleep(5)
            assert True
            self.driver.close()
            self.logger.info("***************test login page passed*******************")
        except:
            self.driver.quit()
            self.logger.info("***************slider test failed*******************")
            assert False