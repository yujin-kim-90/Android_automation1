#인증 > 네이버인증
#import OpenCV
import pytest
import time
# import os
# import sys
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import common
from 변수 import 변수
from 변수 import 변수_인증
from 변수 import secure_keypad
from 변수 import 변수_자산
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

def test_자산진입(driver):
    driver.find_element(By.XPATH, 변수.운영앱).click()
    time.sleep(10)
    # common.swipe_action()
    driver.find_element(By.XPATH, 변수_자산.자산xpath).click()
    print("\n자산 탭 진입 완료")
def test_자산추가(driver):
    time.sleep(10)
    common.swipe_action(driver)
    time.sleep(10)
    driver.find_element(By.XPATH, 변수_자산.자산추가xpath).click()
    time.sleep(10)
    driver.find_element(By.XPATH, 변수_자산.자산추가_은행_xpath).click()
    time.sleep(10)
    driver.find_element(By.XPATH, 변수_자산.연결기관첫번째xpath).click()
    driver.find_element(By.XPATH, 변수_자산.연결하기xpath).click()
    time.sleep(10)
    common.swipe_action(driver)
    time.sleep(10)
    driver.find_element(By.XPATH, 변수_자산.동의xpath).click()
def test_네이버인증(driver):
    time.sleep(10)
    print("\n네이버인증 선택")
    driver.find_element(By.XPATH, 변수_자산.네이버인증xpath).click()
    time.sleep(3)
    driver.find_element(By.XPATH, 변수_자산.네이버인증동의xpath).click()
    driver.find_element(By.XPATH, 변수_자산.네이버인증서동의xpath).click()
    time.sleep(20)
    common.xyTouch(driver,535,1202)
    common.xyTouch(driver,535,2404)
    #driver.find_element(By.XPATH, 변수_자산.네이버인증개인정보동의xpath).click()
    #driver.find_element(By.XPATH, 변수_자산.네이버인증개인정보동의다음xpath).click()
    time.sleep(10)
    print("네이버인증서 비밀번호 입력")
    driver.find_element(By.XPATH, 변수_자산.네이버5).click()
    driver.find_element(By.XPATH, 변수_자산.네이버2).click()
    driver.find_element(By.XPATH, 변수_자산.네이버0).click()
    driver.find_element(By.XPATH, 변수_자산.네이버6).click()
    driver.find_element(By.XPATH, 변수_자산.네이버0).click()
    driver.find_element(By.XPATH, 변수_자산.네이버0).click()
    print("네이버인증 완료")
    time.sleep(20)
    str1=driver.find_element(By.XPATH, 변수_자산.비교문구xpath).text

    assert str1=="연결할 자산을 선택해주세요"





