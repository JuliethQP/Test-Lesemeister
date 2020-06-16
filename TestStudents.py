from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.action_chains import ActionChains

from loginPage import LoginPage  
from staticsPage import StaticPage
from studentPage import StudentsPage
from bookshelfPage import BookshielfPage


class StudentTest(unittest.TestCase):
    
    def setUp(self): 
        self.driver=webdriver.Chrome(executable_path=r'C:\seleniumWebdrivers\chromedriver.exe')
              
    def test_students(self):   
        driver=self.driver    
        driver.get('https://lesemester.no/logg-inn/')        
        driver.maximize_window()  
        time.sleep(3)        
        login=LoginPage(driver)   
        login.enter_username("baerum-teacher19")
        login.enter_password("TestLesemester2020")
        time.sleep(2)
        login.click_login_page_login()
        students= StudentsPage(driver)
        time.sleep(7)
        students.click_tab_students()
        
        
        time.sleep(4)
        statics=StaticPage(driver)
        time.sleep(2)
        statics.filter_period()
        time.sleep(2)
        statics.select_data_filter_from()
        time.sleep(3)    
        statics.select_data_filter_to()
        time.sleep(3)      
        driver.find_element_by_xpath("//div[contains(text(),'Remove all filters')]").click()       
        time.sleep(4)
        driver.find_element_by_class_name("fullWidth").click()
        time.sleep(3)
        driver.find_element_by_xpath("//div[contains(text(),'BOOK ACTIVITY')]").click()
        time.sleep(3)
        driver.find_element_by_class_name("studentDetailsGoBackButton").click()
        time.sleep(3)
        driver.find_element_by_xpath("//div[contains(@class,'selectContainer latoFont studentsTabFilterGroupSelector')]//div[contains(@class,'selectValueComponent centerVertically')]").click()
        options= driver.find_elements_by_class_name("selectOptionText")
        options[1].click()
        time.sleep(3)
        students.filter_by_student_click("10")
        time.sleep(4)
        students.clear_filter()
        time.sleep(2)
    
          
         
    
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print(f"test completed")
        
        
#unittest.main() 
if  __name__=='__main_':
       unittest.main()

   
    
  
   
 
       