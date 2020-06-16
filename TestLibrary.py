from selenium import webdriver
import time
import unittest

from startPage import StartPage
from homePage import HomePage
from loginPage import LoginPage  
from libraryPage import libraryPage
from bookshelfPage import BookshielfPage


class LibraryTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls): 
        cls.driver=webdriver.Chrome(executable_path=r'C:\seleniumWebdrivers\chromedriver.exe')
        
    def test_library(self):
    #INDICATE THE LINK TO DRIVER
        driver=self.driver
        driver.set_window_size(1024, 600)
        driver.maximize_window()
        driver.get('https://lesemester.no/')
        driver.implicitly_wait(5)
        #USING STARPAGE CLASS
        start=StartPage(driver)
        start.click_login()
        time.sleep(3)
    #USING LOGINPAGE CLASS         
        login=LoginPage(driver)    
        login.enter_username("baerum-teacher19")
        login.enter_password("TestLesemester2020")
        login.click_login_page_login()
        time.sleep(2)
        
        library=libraryPage(driver)
        library.click_library()
        time.sleep(2)
        library.click_select_book_by_className()
        book_name_library = library.capture_name_book_select()
        time.sleep(5)
        print("book name from library:")
        print(book_name_library)
        time.sleep(2)
        library.click_add_book_to_group()
        time.sleep(2)
        library.click_select_group()
        time.sleep(2)
        library.verify_details_book()
        time.sleep(2)
        library.click_add_book_challenge()  
        time.sleep(4)
        bookshelf = BookshielfPage(driver)
        time.sleep(2)
        bookshelf.click_bookshelf()
        time.sleep(2)
              
        book_name_bookshelf =bookshelf.capture_name_book()
        time.sleep(5)
        print("book name from bookshelf")
        print(book_name_bookshelf)
        
        if (book_name_bookshelf == book_name_library):
            print("book added success")   
        
        library.click_library()
        library.search_book_by_name("a good idea")    
        time.sleep(3)
        library.click_select_book_by_className()
        time.sleep(3)
        library.click_add_book_to_group()
        time.sleep(3)
        driver.find_element_by_class_name("cancelAddBookToClass").click()
        time.sleep(3)
        driver.find_element_by_class_name("bookTabFilterGoBackButton").click()
        time.sleep(3)
        library.search_book_by_name("Apropos forelska")  
        time.sleep(3)         
        driver.find_element_by_class_name("bookCoverContainer").click()
        time.sleep(3)
        driver.find_element_by_class_name("bookProfileStartReadingButton").click()
        time.sleep(7)
        
        
       
        
   
        
    @classmethod  
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")   
             
unittest.main()
#if  __name__=='__main_':
   
   
       