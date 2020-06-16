from random import randint, uniform,random
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from startPage import StartPage
from homePage import HomePage
from loginPage import LoginPage  
from bookshelfPage import BookshielfPage
timeout=30

class BookTest(unittest.TestCase):
    
    def setUp(self): 
       
        self.driver= webdriver.Chrome(r'C:\seleniumWebdrivers\chromedriver.exe')
    
    def test_book_valid(self): 
                      
        driver=self.driver
        driver.maximize_window()
        driver.get('https://lesemester.no/')
        driver.implicitly_wait(5)
        driver.get('https://lesemester.no/logg-inn/')
        login=LoginPage(self.driver)    
        login.enter_username("baerum-teacher19")
        time.sleep(1)
        login.enter_password("TestLesemester2020")
        login.click_login_page_login()         
   
        try:
            element_present = EC.presence_of_element_located((By.XPATH, "//div[@id='root']/div[2]/div/div[3]/div[3]/div/div"))  
                 
            WebDriverWait(self.driver, timeout).until(element_present)        
        except TimeoutException:          
            print ("Timed out waiting for page to load")   
                                
        bookshelf=BookshielfPage(self.driver)
        time.sleep(4)
        bookshelf.click_bookshelf()
        time.sleep(3) 
        bookshelf.click_icon_add_book()
        nums_books = driver.find_elements_by_class_name("bookCoverAddBookIcon")
        nums_books_len = len(nums_books)
        print(nums_books_len)
        num_random_book = randint(0,nums_books_len)
        time.sleep(3)
        nums_books[num_random_book].click()
        time.sleep(3)
        bookshelf.click_button_select_add()
        time.sleep(3)
        bookshelf.select_book_by_className()
        time.sleep(3)
        bookshelf.click_button_new_challenge()
        time.sleep(3)
        bookshelf.create_new_challenge_select_student_by_group()
        time.sleep(5) 
        message_success= self.driver.find_element_by_class_name("notificationItemMessage").text             
        self.assertTrue(message_success == "Challenge sent")
        time.sleep(3)
        driver.find_element_by_class_name("bookTabFilterGoBackButton").click()
        
        bookshelf.change_group()    
        bookshelf.filter_by_language()
        bookshelf.filter_by_genre()    
        bookshelf.filter_by_level()
        time.sleep(2)
        bookshelf.filter_by_sound()
        bookshelf.filter_by_quiz()
        bookshelf.click_remove_filter()
        time.sleep(2)
        bookshelf.click_toggle_filter_button()
        time.sleep(2)        
        element = driver.find_element_by_class_name("bookCoverImage")      
        ActionChains(driver).click_and_hold(element).perform()
        time.sleep(3)
        driver.find_element_by_class_name("bookCoverRemoveBookIcon").click()
        time.sleep(3)
        driver.find_element_by_class_name("deleteBookModalOkButton").click()
        time.sleep(3)   
        
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print(f"test completed")

unittest.main()
 
if  __name__ =='__main_':
    print('main it is running')
       