from Selenium import webdriver
from Selenium.webdriver.common.by import By
from Test_Data import data
import pytest
import time


class Test_Ham:
    url:"https://opensource-demo.orangehrmlive.com/"

@pytest.fixture

def booting_function (self):
    self.driver = webdriver.Firefox()
    yield
    self.driver.close()

def test_get_title (self, booting_function):
    self.driver.get (self.url)
    assert self.driver.title == 'OrangeHRM'
    print ("SUCCESS #web title captured successfully")

def test_login (self, booting_function):
    self.driver.get(self.url)
    time.sleep(5)
    self.driver.find_element(by= BY.NAME, value =  data.Hamritha_Selectors.input_box_username).send_keys (data.Hamritha_Data.username)
    self.driver.find_element(by= BY.NAME, value =  data.Hamritha_Selectors.input_box_password).send_keys (data.Hamritha_Data.password)
    self.driver.find_element(by= By.XPATH,value =  data.Hamritha_Selectors.login_XPATH).click()
    assert self.driver.title == 'OrangeHRM'
