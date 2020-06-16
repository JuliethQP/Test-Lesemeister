from selenium.webdriver.support.ui import Select
import time
class BookshielfPage():
    
    #constructor 
    def __init__(self,driver):
        
        self.driver=driver
        self.bookshielf_tab="//div[@id='root']/div[2]/div/div[3]/div[3]/div/div"
        self.icon_add_xpath="//*[@id='root']/div[4]/div/div/div[1]"
        self.add_book_className="bookCoverImage"
        self.button_add_select_xpath="//*[@id='root']/div[3]/div[1]/div[4]"
        self.input_search_xpath="searchInput displayNone"         
        self.group_teacher_xpath="//*[@id='root']/div[3]/div[1]/div[4]/div"
        
    def click_bookshelf(self):
        self.driver.find_element_by_xpath(self.bookshielf_tab).click()
        
    def click_icon_add_book(self):
        self.driver.find_element_by_xpath(self.icon_add_xpath).click()
       
    def select_book_by_className(self):
        self.driver.find_element_by_class_name(self.add_book_className).click()
    
    def click_button_select_add(self):
        self.driver.find_element_by_xpath(self.button_add_select_xpath).click()
        
    def enter_name_book_by_filter(self,nameBook):
        self.driver.find_element_by_xpath(self.input_search_xpath).click()
        self.driver.find_element_by_xpath(self.input_search_xpath).send_keys(self.nameBook)  
    
    def count_book(self):   
        
        print(f"hello world")     
        books = self.driver.find_elements_by_class_name("bookTitle")
        authors = self.driver.find_elements_by_class_name("bookAuthor")
        num_books = len(books)
        return (self.num_books)
        #for i in range(num_books):      
        #    print(f"{books[i].text:<50}\t{authors[i].text:<50}")
           
    
    def change_group(self):        
        options = self.driver.find_element_by_class_name("selectContainer")
        options.click()
        time.sleep(3)
        select_option = self.driver.find_elements_by_class_name("selectOptionText")
        select_option_len = len(select_option)
        select_option[0].click()
        for i in range (select_option_len):
            options = self.driver.find_element_by_class_name("selectContainer")
            options.click()
            time.sleep(5)
            select_option = self.driver.find_elements_by_class_name("selectOptionText")
            print(f"{select_option[i].text}")
            select_option[i].click()
            time.sleep(5)
            
    def filter_by_language(self):
        options = self.driver.find_element_by_class_name("booksTabFilterLanguageSelector").click()        
        time.sleep(3)
        language_option = self.driver.find_elements_by_class_name("selectOptionText")
        count_language=len(language_option)
        print(f"{language_option[3].text}")
        language_option[3].click()
        time.sleep(3)   
         
    def filter_by_genre(self):
        options = self.driver.find_element_by_class_name("booksTabFilterGenreSelector").click()        
        time.sleep(3)
        language_option = self.driver.find_elements_by_class_name("selectOptionText")
        count_language=len(language_option)
        print(f"{language_option[1].text}")
        language_option[1].click()
        time.sleep(3) 
        
    def filter_by_level(self):
        options = self.driver.find_element_by_class_name("booksTabFilterLevelSelector").click()        
        time.sleep(3)
        language_option = self.driver.find_elements_by_class_name("selectOptionText")
        count_language=len(language_option)
        print(f"{language_option[2].text}")
        language_option[2].click()
        time.sleep(3) 
        
    def filter_by_sound(self):
        options = self.driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[3]/div[2]/div[4]").click()        
        time.sleep(3)
        language_option = self.driver.find_elements_by_class_name("selectOptionText")
        count_language=len(language_option)
        print(f"{language_option[1].text}")
        language_option[1].click()
        time.sleep(3) 
        
    def filter_by_quiz(self):         
        options = self.driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[3]/div[2]/div[5]").click()        
        time.sleep(3)
        language_option = self.driver.find_elements_by_class_name("selectOptionText")
        count_language=len(language_option)
        print(f"{language_option[1].text}")
        language_option[1].click()
        time.sleep(3) 
            
    def click_remove_filter(self):
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[3]/div[2]/div[9]/div[1]").click()
            
    def click_toggle_filter_button(self):    
        self.driver.find_element_by_xpath("//div[contains(@class,'baseButton toggleFilterButton')]//img[contains(@class,'imgButtonImage')]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//div[contains(@class,'baseButton toggleFilterButton')]//img[contains(@class,'imgButtonImage')]").click()
    
    def click_button_new_challenge(self):
        self.driver.find_element_by_xpath("//div[@class='baseButton bookProfileStartReadingButton center']").click()
    
    def create_new_challenge_select_student_by_group(self):
        options = self.driver.find_element_by_class_name("bookProfileSelectClass").click()        
        time.sleep(3)
        student = self.driver.find_elements_by_class_name("selectOptionText")
        count_student = len(student)
        time.sleep(3)
                
        for i in range (count_student):                   
            print(f"{student[i].text}")
            
        student[-1].click()    
        self.driver.find_element_by_xpath("//div[@class='baseButton bookProfileOnCreateChallenge center']").click()
        #verify success add challenge 
        
    def capture_name_book(self):
        name_book = self.driver.find_element_by_class_name("bookTitle").text
        return(name_book)
           
        
    
       
       
        
            
            
            
      
        
    
         
        
    #def click_filter_area_books(self):        
        
       
               
                
     
        
        