from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.action_chains import ActionChains

from loginPage import LoginPage  
from staticsPage import StaticPage


class StacticTest(unittest.TestCase):
    
    def setUp(self): 
        self.driver=webdriver.Chrome(executable_path=r'C:\seleniumWebdrivers\chromedriver.exe')
              
    def test_statistics(self):   
        driver=self.driver    
        driver.get('https://lesemester.no/logg-inn/')        
        driver.maximize_window()  
        time.sleep(3)        
        login=LoginPage(driver)   
        login.enter_username("baerum-teacher19")
        login.enter_password("TestLesemester2020")
        time.sleep(2)
        login.click_login_page_login()
        time.sleep(2)   
        statics=StaticPage(driver)
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")        
        time.sleep(8)
        statics.filter_period()
        time.sleep(3) 
        statics.select_data_filter_from()
        time.sleep(3)    
        statics.select_data_filter_to()    
        time.sleep(6)          
         
    
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print(f"test completed")
        
        
#unittest.main() 
if  __name__=='__main_':
       unittest.main()

   
    
  
   
 
       