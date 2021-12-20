import random
import time
from datetime import datetime, timedelta
import unittest
from selenium.webdriver.common.by import By

class PageMain():
    def __init__(self,myDriver):
        self.driver = myDriver
        self.generate_ramdon_date()
        self.agree_button = (By.ID, 'didomi-notice-agree-button')
        self.destination_box = (By.ID, 'mbe-destination-input')
        self.date_box = (By.ID, 'mbe-dates-select')
        self.in_date = (By.XPATH, "//li[contains(@class,'"+self.startSearch+"')]")
        self.out_date = (By.XPATH, "//li[contains(@class,'"+self.endSearch+"')]")
        self.search_button = (By.ID, 'mbe-search-button')
        
        
    def strTime(self, start, end, format, prop):
        stime = time.mktime(time.strptime(start, format))
        etime = time.mktime(time.strptime(end, format))
    
        ptime = stime + prop * (etime - stime)
    
        return time.strftime(format, time.localtime(ptime))

    def randomDate(self, start, end, prop):
        return self.strTime(start, end, '%Y-%m-%d', prop)
    
    def generate_ramdon_date(self):
        startDate = datetime.today().strftime('%Y-%m-%d')
        endDate = (datetime.today() + timedelta(days=30)).strftime('%Y-%m-%d')
        self.startSearch = self.randomDate(startDate, endDate, random.random())
        self.endSearch = (datetime.strptime(self.startSearch,'%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')
        
    def accept_terms_conditions(self):
        self.driver.find_element(*self.agree_button).click()
    
    def search_hotel(self, hotel):
        self.driver.find_element(*self.destination_box).click()
        self.driver.find_element(*self.destination_box).send_keys(hotel)
        
    def select_dates(self):
        self.driver.find_element(*self.date_box).click()
        self.driver.find_element(*self.in_date).click()
        self.driver.find_element(*self.out_date).click()
        
    def search_availability_hotel(self):
        self.driver.find_element(*self.search_button).click()
        
    def verify_search(self):
        tc = unittest.TestCase('__init__')
        urlNext = "https://booking.melia.com/es/new/buscar/hoteles-disponibles.htm"
        a = self.driver.current_url
        tc.assertEqual(urlNext, self.driver.current_url)
        
        
        