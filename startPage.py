from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class StartPage():
    
    #constructor 
    def __init__(self,driver):
        
        self.driver=driver
        self.link_login_class_name="current_page_item menu-item-3895"
        
    def click_login(self):       
        self.driver.find_element_by_id("menu-item-3895").click()
     
        
  