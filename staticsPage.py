import time
class StaticPage():
    
    def __init__(self,driver):
        self.driver=driver
        self.period_filter_class="timeFilterSelectPeriod "
        
    def filter_period(self):       
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]").click()
        time.sleep(3) 
        options=self.driver.find_elements_by_class_name("selectOptionText")
        time.sleep(3)       
        count_options=len(options)       
        options[-1].click()
        time.sleep(3) 
        
    def select_data_filter_from(self):
        self.driver.find_element_by_xpath("//div[@class='timeFilterDatePicker']").click()
        time.sleep(3)
        self.driver.find_element_by_class_name("react-datepicker__navigation--previous").click()
        time.sleep(3)
        self.driver.find_element_by_class_name("react-datepicker__day--014").click()
        
    def select_data_filter_to(self):
        self.driver.find_element_by_xpath("//div[contains(@class,'timeFilterDatePicker timeFilterDatePickerRight')]//div[contains(@class,'react-datepicker__input-container')]").click()
        time.sleep(3)
        self.driver.find_element_by_class_name("react-datepicker__day--016").click()
        time.sleep(3)
        
        