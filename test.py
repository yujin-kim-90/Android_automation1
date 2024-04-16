

str= ("4월 16일 결제예정금액")
str1=str[7:13]
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


    str= driver.find_element(By.XPATH, 변수_홈.결제예정금액타이틀xpath).text
    print(str)
