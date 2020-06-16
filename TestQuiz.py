from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.action_chains import ActionChains

from loginPage import LoginPage  
from staticsPage import StaticPage


class QuizTest(unittest.TestCase):
    
    def setUp(self): 
        self.driver=webdriver.Chrome(executable_path=r'C:\seleniumWebdrivers\chromedriver.exe')
              
    def test_quiz(self):   
        driver=self.driver    
        driver.get('https://lesemester.no/logg-inn/')        
        driver.maximize_window()  
        time.sleep(3)        
        login=LoginPage(driver)   
        login.enter_username("baerum-teacher19")
        login.enter_password("TestLesemester2020")
        time.sleep(2)
        login.click_login_page_login()
        time.sleep(7)   
        driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/div[3]/div[5]/div[1]").click()
        time.sleep(3)
        driver.find_element_by_xpath("//div[contains(@class,'selectContainer latoFont quizFilterViewsSelectionSelector')]//img[contains(@class,'selectArrow')]").click()
        options= driver.find_elements_by_class_name("selectOptionText")
        time.sleep(3)
        options[1].click()
        time.sleep(3)
        driver.find_element_by_xpath("//div[contains(@class,'selectContainer latoFont quizFilterViewsSelectionSelector')]//img[contains(@class,'selectArrow')]").click()
        time.sleep(4)
        options= driver.find_elements_by_class_name("selectOptionText")
        options[0].click()
        time.sleep(3)
        
        driver.execute_script("window.scrollTo(0, 2000)")    
        time.sleep(3)
        driver.execute_script("window.scrollTo(2000, 0)")   
        time.sleep(3)       
        driver.find_element_by_class_name("quizFilterEnableQuizButton").click()
        time.sleep(5)
        driver.find_element_by_class_name("quizFilterEnableQuizButton").click()
        time.sleep(3)
        driver.find_element_by_class_name("searchContainer").click()
        time.sleep(2)
        driver.find_element_by_class_name("searchInput").send_keys("10")
        time.sleep(4)
        driver.find_element_by_class_name("searchInput").clear()
        time.sleep(3)
    
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print(f"test completed")
        
        
#unittest.main() 
if  __name__=='__main_':
       unittest.main()

   
    
  
   
 
       