import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils

from selenium.webdriver.common.action_chains import ActionChains
import time


class Test_002_ddt_Login:
    baseUrl = ReadConfig.getApplicationURL()
    path = "C:/Users/mperiyasamy/PycharmProjects/infor/TestData/LoginData.xlsx"
    # TestData / LoginData.xlsx
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

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("************************Test_002_ddt_Login******************************")
        self.logger.info("***************Verifying Login ddt testing*******************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        lst_status = []

        for r in range(2, self.rows + 1):
            self.username = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.lp.user_login(self.username, self.password)
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info("****************Passed**********************")
                    self.lp.Logout()
                    lst_status.append("Pass")
                elif self.exp == 'fail':
                    self.logger.info("**** failed ****")
                    self.lp.Logout()
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** failed ****")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("**** passed ****")
                    lst_status.append("Pass")
            print(lst_status)
        if "Fail" not in lst_status:
            self.logger.info("******* DDT Login test passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("******* DDT Login test failed **********")
            self.driver.close()
            assert False

        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ")


    # def test_slider(self, setup):
    #     self.logger.info("***************Verifying Slider testing*******************")
    #     self.driver = setup
    #     self.driver.get(self.baseUrl)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.user_login(self.username, self.password)
    #     try:
    #         self.lp.image_main_logo()
    #         time.sleep(5)
    #         self.driver.execute_script("window.scrollBy(0,500)")
    #         time.sleep(5)
    #         assert True
    #         self.driver.close()
    #         self.logger.info("***************test login page passed*******************")
    #     except:
    #         self.driver.quit()
    #         self.logger.info("***************slider test failed*******************")
    #         assert False
