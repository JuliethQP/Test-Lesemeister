class HomePage():
    
    def __init__(self,driver):
        self.driver=driver
        self.user_img_xpath="//*[@id='root']/div[2]/div/div[5]/div/img"
        self.logout_xpath="//div[@id='root']/div[2]/div/div[6]/div[11]/div/div"
        
    def click_welcome(self):
       
        self.driver.find_element_by_xpath(self.user_img_xpath).click() 
        
    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_xpath).click()
           

