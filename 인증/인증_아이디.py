#인증 > 아이디

from 변수 import 변수
from 변수 import 변수_인증
import common
import pytest
import time
import os

from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def driver():
    capabilities = dict(
        platformName='Android',
        automationName='uiautomator2',
    )
    appium_server_url = 'http://localhost:4723/wd/hub'
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    driver.press_keycode(3)
    yield driver
    driver.quit()


#tc_id: log_33
def test_case_01(driver)->None:
    driver.find_element(By.XPATH, 변수.개발계앱).click()
    driver.find_element(By.ID, 변수_인증.아이디비번설정id).click()
    time.sleep(3)
    driver.find_element(By.XPATH, 변수_인증.본인인증휴대폰).click()
    time.sleep(3)
    # driver.find_element(By.XPATH, 변수.앱이름).click()
    # time.sleep(3)
    common.휴대폰인증(driver)
    time.sleep(10)

    str1=driver.find_element(By.ID, 변수_인증.간편번호설정문구확인id).text
    assert str1=="아이디/비밀번호 입력"

def test_case_04(driver)-> None:
    driver.find_element(By.ID, 변수_인증.아이디입력id).send_keys("autotest1")
    driver.find_element(By.ID, 변수_인증.비번입력id).click()
    common.아이디비밀번호설정(driver)
    driver.find_element(By.ID, 변수_인증.비번확인id).click()
    common.아이디비밀번호설정(driver)
    driver.find_element(By.ID, 변수_인증.확인버튼id).click()






