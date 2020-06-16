from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException  

from startPage import StartPage
from homePage import HomePage
from loginPage import LoginPage  


class LoginTest(unittest.TestCase):
    
    def setUp(self): 
        self.driver=webdriver.Chrome(executable_path=r'C:\seleniumWebdrivers\chromedriver.exe')
       
    def test_login_valid(self):
        driver=self.driver     
        driver.get('https://lesemester.no/logg-inn/')
        driver.set_window_size(1024, 600)
        driver.maximize_window()
        driver.implicitly_wait(5)       
        time.sleep(3)     
        login=LoginPage(driver)    
        login.enter_username("baerum-teacher19")
        login.enter_password("TestLesemester2020")
        login.click_login_page_login()
        time.sleep(2)       
        homepage=HomePage(driver)
        time.sleep(4)
        homepage.click_welcome()
        time.sleep(3)       
        homepage.click_logout()
        time.sleep(3)   
             
    def test_login_invalid_username(self):       
        driver=self.driver     
        start=StartPage(driver)     
        driver.get('https://lesemester.no/logg-inn/')
        
        driver.maximize_window()  
        time.sleep(3)
        #driver.implicitly_wait(5) 
        try:
            driver.find_element_by_id("menu-item-3895")
        except NoSuchElementException:
            print ("yes") 
        print("not")  
        time.sleep(3)        
        login=LoginPage(driver)    
        time.sleep(2)
        login.enter_username("baeru-teacher")
        time.sleep(2)
        login.enter_password("TestLesemester2020")
        time.sleep(2)
        login.click_login_page_login()
        time.sleep(2)   
        message_invalid = self.driver.find_element_by_id("errorMsg").text    
        time.sleep(3)         
        self.assertTrue(message_invalid == "Brukernavn eller passord er feil")
        time.sleep(3)
            
    def test_login_invalid_password(self):   
        driver=self.driver     
        start=StartPage(driver)     
        driver.get('https://lesemester.no/logg-inn/')        
        driver.maximize_window()  
        time.sleep(1)
        try:
            driver.find_element_by_id("menu-item-3895")
        except NoSuchElementException:
            print ("not") 
        print("yes")  
        time.sleep(3)        
        login=LoginPage(driver)    
        time.sleep(2)
        login.enter_username("baerum-teacher19")
        time.sleep(2)
        login.enter_password("testLesemester2020")
        time.sleep(2)
        login.click_login_page_login()
        time.sleep(2)   
        message_invalid = self.driver.find_element_by_id("errorMsg").text    
        time.sleep(3)         
        self.assertTrue(message_invalid == "Brukernavn eller passord er feil")
        time.sleep(3)   
    
    #el decorador sirve para saltarse la prueba    
    #@unittest.skipIf(True,"nuestros motivos")   #el primer argumento, si es true se ejecuta sino no se ejcuta, tambien se puede poner algo como 8>3 -->True   
    def test_invalid_login(self):   
        driver=self.driver     
        start=StartPage(driver)     
        driver.get('https://lesemester.no/logg-inn/')        
        driver.maximize_window()  
        time.sleep(3)
        try:
            driver.find_element_by_id("menu-item-3895")
        except NoSuchElementException:
            print ("yes") 
        print("not")  
        time.sleep(3)        
        login=LoginPage(driver)    
        time.sleep(2)
        login.enter_username("baerum")
        time.sleep(2)
        login.enter_password("testLesemester")
        time.sleep(2)
        login.click_login_page_login()
        time.sleep(2)   
        message_invalid = self.driver.find_element_by_id("errorMsg").text    
        time.sleep(3)         
        self.assertTrue(message_invalid == "Brukernavn eller passord er feil")
       
    
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print(f"test completed")
        
if  __name__=='__main_':
    unittest.main()

   
    
  
   
 
       