#인증 > 간편번호(휴대폰 인증)
import common
from 변수 import 변수
from 변수 import 변수_인증
from 변수 import 변수_홈
import OpenCV
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

#tc_id: home_01
def test_case_01(driver)->None:
    driver.find_element(By.XPATH, 변수.앱이름).click()
    time.sleep(30)
    str1=driver.find_element(By.XPATH, 변수_인증.홈확인).text
    assert str1=="홈"

#tc_id: home_04
def test_case_02(driver)->None:
    driver.find_element(By.XPATH, 변수_홈.결제예정금액xpath).click()
    str= driver.find_element(By.XPATH, 변수_홈.결제예정금액타이틀xpath).text
    print(str)
    str1=str[7:13]
    assert str1=="결제예정금액"
#tc_id: home_03
def test_case_03(driver)->None:
    driver.find_element(By.XPATH, 변수_홈.결제예정금액이전버튼xpath).click()
    driver.find_element(By.XPATH, 변수_홈.즉시결제xpath).click()
    str=driver.find_element(By.XPATH, 변수_홈.바로출금타이틀xpath).text
    assert str=="바로출금"



# def test_case_04(driver)->None:





