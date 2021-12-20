import unittest
from selenium.webdriver.common.by import By


class PageRooms():
    def __init__(self,myDriver):
        self.driver = myDriver
        self.agree_button = (By.ID,'didomi-notice-agree-button')
        self.rooms = (By.CLASS_NAME,'c-hotel-sheet-room__content-name')
        
    def accept_terms_conditions(self):
        self.driver.find_element(*self.agree_button).click()
    
    def select_rooms_available(self):
        return self.driver.find_elements(*self.rooms)
    
    def show_rooms_available(self):
        for room in self.driver.find_elements(*self.rooms):
            print(room.text)
        print("El total de habitaciones es: "+str(len(self.driver.find_elements(*self.rooms))))
    
    def verify_rooms_available(self):
        tc = unittest.TestCase('__init__')
        tc.assertGreater(len(self.select_rooms_available()), 0)