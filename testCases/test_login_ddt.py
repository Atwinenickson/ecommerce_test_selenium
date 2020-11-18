from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.ods"

    logger = LogGen.loggen()
    def test_login_ddt(self, setup):
        self.logger.info(" ************* Test__002__DDT__Login*********** ")
        self.logger.info(" ******************** Veryfying after login ddt test title *************** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of rows in excel file:", self.rows)


        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r,1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)








        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info(" ********************* After login title passed *************** ")
        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_login.png")
            self.driver.close()
            self.logger.error(" ********************************* After login title test failed ********************* ")
            assert False