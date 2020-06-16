        
        
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.action_chains import ActionChains

from loginPage import LoginPage  
from staticsPage import StaticPage


class MainTest(unittest.TestCase):    
    
    def setUp(self): 
        self.driver=webdriver.Chrome(executable_path=r'C:\seleniumWebdrivers\chromedriver.exe')
              
    def test_main(self):      
        driver = self.driver
        driver.get("https://lesemester.no/")
        driver.maximize_window()  
        time.sleep(3)
        driver.find_element_by_xpath("//li[@id='menu-item-3887']").click()
        time.sleep(3)
        driver.execute_script("window.scrollTo(0, 2500)")   
        time.sleep(3)
        driver.execute_script("window.scrollTo(2000, 0)") 
        time.sleep(3) 
        driver.find_element_by_id("menu-item-479").click()
        time.sleep(4)
        driver.find_element_by_xpath("//li[@id='menu-item-3887']").click()          
        driver.find_element_by_id("menu-item-476").click()
        time.sleep(4)
        driver.execute_script("window.scrollTo(0, 2500)")  
        time.sleep(2)
        driver.execute_script("window.scrollTo(2500, 0)")  
        time.sleep(3)  
        driver.find_element_by_xpath("//li[@id='menu-item-3887']").click()      
        driver.find_element_by_id("menu-item-1238").click()
        time.sleep(3)
        driver.execute_script("window.scrollTo(0, 2500)")   
        time.sleep(3)
        driver.execute_script("window.scrollTo(2500, 0)") 
        time.sleep(3)  
        driver.find_element_by_id("menu-item-3886").click() #skole
        time.sleep(3)              
        driver.find_element_by_id("menu-item-1117").click() #blog
        time.sleep(4)  
        driver.find_element_by_xpath("//li[@id='menu-item-wpml-ls-9-bl']").click() #bokmal
        time.sleep(4)           
        driver.find_element_by_xpath("//*[contains(@href,'/sign-up-1-bestill')]").click() #Bestill
        driver.execute_script("window.scrollTo(0, 2500)") 
        time.sleep(3)
        driver.execute_script("window.scrollTo(0, 2500)") 
        time.sleep(7)          
     
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print(f"test completed")
        
        
#unittest.main() 
if  __name__=='__main_':
       unittest.main()