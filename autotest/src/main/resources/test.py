'''
Created on 17 dic 2021

@author: Borja Borrallo
'''
# coding=UTF-8
import unittest
from selenium import webdriver

from Pages.PageMain import * 
from Pages.PageRooms import *


class TestMelia(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.maximize_window()
        self.PageMain = PageMain(self.driver)
        self.PageRooms = PageRooms(self.driver)
        
    def test_searchHotel(self):
        self.driver.get('https://www.melia.com')
        self.driver.implicitly_wait(5)
        self.PageMain.accept_terms_conditions()
        self.PageMain.search_hotel('madrid')
        self.PageMain.select_dates()
        self.PageMain.search_availability_hotel()
        self.PageMain.verify_search()


    def test_roomList(self):
        self.driver.get('https://www.melia.com/es/hoteles/espana/madrid/melia-castilla/habitaciones.htm')
        self.driver.implicitly_wait(5)
        self.PageRooms.accept_terms_conditions()
        self.PageRooms.show_rooms_available()
        self.PageRooms.verify_rooms_available()

        
    def tearDown(self):
        self.driver.quit()
        
    
