import time
class StudentsPage():
    
    def __init__(self,driver):
        self.driver=driver
        self.filter_by_student_xpath="//div[contains(@class,'searchContainer centerVertically latoFont')]"
    
    def click_tab_students(self):
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[1]/div[3]/div[2]/div[1]").click()
        
    def filter_by_student_click(self,keywords):  
        self.driver.find_element_by_xpath(self.filter_by_student_xpath).click()
        self.driver.find_element_by_class_name("searchInput").send_keys(keywords)
        student = self.driver.find_element_by_class_name("studentProfileStudentName")
        print(f"{student.text}")
    
    
    def clear_filter(self):
        self.driver.find_element_by_class_name("searchInput").clear()
    
         
    
        
               
 
        
        