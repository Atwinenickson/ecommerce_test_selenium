from selenium import webdriver

class LoginPage:
    textbox_username_id="Email"
    textbox_password_id="Password"
    button_login_xpath="//body/div[6]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[3]/input[1]"
    link_logout_linktext="Logout"

    def __init__(self, driver):
        self.driver = driver
    
    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    
    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    
    def clickLogin(self):
        try:
            self.driver.find_element_by_xpath(self.button_login_xpath).click()
        except:
            print('un expected exception found. no expath found')
        

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()