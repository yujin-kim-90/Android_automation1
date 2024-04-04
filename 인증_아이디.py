import 변수
import 변수_인증
import 변수_로그인
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

#여기서 현재경로 보여주고
currentPath = '%s/' % os.getcwd()
screenshotPath = currentPath + '%s-screenshot.png'

#tc_id: log_33
def test_case_01(driver)->None:
    driver.find_element(By.ID, 변수_인증.다른로그인방법id).click()
    driver.find_element(By.XPATH, 변수_인증.로그인방법_아이디).click()
    driver.find_element(By.ID, 변수_인증.아이디비번설정id).click()
    str1=driver.find_element(By.ID, 변수_인증.간편번호설정문구확인id).text

    assert str1=="본인 인증"

#tc_id: log_34
def test_case_02(driver)->None:
    driver.find_element(By.XPATH, 변수.앱이름).click()
    for i in range(len(변수.카드번호)):
        #driver.find_element(By.XPATH, 변수_인증.카드번호입력id).click()
        str="//android.widget.ImageView[@content-desc="""+변수.카드번호[i]+"]"""
        driver.find_element(By.XPATH,str).click()

