from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_Login:
    baseURL = ReadConfig.getUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen().loggen()

    def test_homePage(self, setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.logger.info("**** Home page title test passed ****")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_homePage.png")
            self.logger.error("Home page title is failed")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.logger.info("Testing login")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("Testing login is passed")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_login.png")
            self.logger.error("Testing login is failed")
            self.driver.close()
            assert False


