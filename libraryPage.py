import time
from selenium.common.exceptions import NoSuchElementException   
class libraryPage():
    
    def __init__(self,driver):
        self.driver=driver
        self.library_tab_xpath="/html[1]/body[1]/div[1]/div[2]/div[1]/div[3]/div[4]"
        self.add_book_className="bookCoverImage"
        self.button_add_by_group="bookProfileAddBookToClassButton"
        
    def click_library(self):
        self.driver.find_element_by_xpath(self.library_tab_xpath).click()
        
        
    def click_select_book_by_className(self):
        self.driver.find_element_by_class_name(self.add_book_className).click()
        
    def click_add_book_to_group(self):
        self.driver.find_element_by_class_name(self.button_add_by_group).click()
    
    def click_select_group(self):
        self.driver.find_element_by_class_name("bookProfileSelectClass").click()
        options = self.driver.find_elements_by_class_name("selectOptionText")
        options_len = len(options)
        time.sleep(2)
        options[-1].click()
        
    def click_add_book_challenge(self):
        self.driver.find_element_by_class_name("bookProfileOnAddBookToClass").click()
    
    
    def verify_details_book(self):
        try:
           self.driver.find_element_by_class_name("bookProfileDescriptionAndDetailsTitle")
        except NoSuchElementException:
            print("No se encuentra la eriqueta -Details")
            print(False)
            
        print("Si se encuentra la eriqueta -Details")
        print(True)
       
        informations = self.driver.find_elements_by_class_name("bookProfileDetailValue")
        informations_len = len (informations)
        for i in range(informations_len):
             print(f"{informations[i].text}")
            
    def capture_name_book_select(self):
        book_name = self.driver.find_element_by_class_name("bookProfileBookTitle").text
        return (book_name)
        
        
    def search_book_by_name( self, bookName):
        self.driver.find_element_by_class_name("searchContainer").click()
        self.driver.find_element_by_class_name("searchInput").send_keys(bookName)
    
    def clear_search(self):
        self.driver.find_element_by_class_name("searchInput").clear()
        
        
        
        
        