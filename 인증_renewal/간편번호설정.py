#인증renewal > 간편번호(휴대폰 인증)
#import OpenCV
import pytest
import time
# import os
# import sys
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import common
from 변수 import 변수
from 변수 import 변수_인증
from 변수 import 변수_인증renewal
from 변수 import secure_keypad

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

# def test_간편번호우회(driver)->None:
#     driver.find_element(By.XPATH, 변수.운영앱).click()
#     time.sleep(10)
#     driver.find_element(By.ID, 변수_인증renewal.아이디로그인버튼).click()
#     time.sleep(5)
#     driver.find_element(By.ID, 변수_인증.다른로그인방법id).click()
#     time.sleep(3)
#     driver.find_element(By.ID, 변수_인증renewal.간편번호버튼).click()
#     time.sleep(3)
#     driver.find_element(By.XPATH, 변수_인증renewal.간편번호설정).click()
def test_본인인증(driver)->None:
    driver.find_element(By.XPATH, 변수.운영앱).click()
    time.sleep(10)
    driver.find_element(By.ID, 변수_인증renewal.이름입력).send_keys("김유진")
    driver.press_keycode(66)
    driver.find_element(By.ID, 변수_인증renewal.생년월일).send_keys("900803")
    driver.find_element(By.ID, 변수_인증renewal.주민번호뒷자리).click()
    driver.press_keycode(9)
    driver.find_element(By.XPATH, 변수_인증renewal.skt알뜰폰).click()
    driver.find_element(By.ID, 변수_인증renewal.인증요청).click()
    driver.find_element(By.ID, 변수_인증renewal.휴대폰인증동의).click()
    time.sleep(3)
    # driver.find_element(By.ID, 변수_인증renewal.확인).click()
    # time.sleep(10)

def test_MO인증(driver)->None:
    # driver.find_element(By.XPATH, 변수.운영앱).click()
    # time.sleep(3)
    #common.xyTouch(driver, 487, 1572)
    driver.find_element(By.ID, 변수_인증renewal.MO인증확인).click()
    driver.find_element(By.ID,"com.samsung.android.messaging:id/send_button_icon").click()
    driver.press_keycode(4) # 이전 2번 눌러야해서 키코드 4 2개 넣음
    driver.press_keycode(4)
    time.sleep(5)
    str1=driver.find_element(By.ID, 변수_인증renewal.로카페이타이틀).text
    assert str1=="로카페이"

def test_로카페이설정(driver)->None:
    driver.find_element(By.XPATH, secure_keypad.숫자5).click()
    driver.find_element(By.XPATH, secure_keypad.숫자2).click()

def test_간편번호설정(driver)->None:
    common.간편번호설정(driver)
    time.sleep(20) #문자랑 겹쳐서 일부러 더 넣음

def test_앱메인호출(driver)->None:
    driver.find_element(By.ID, 변수_인증renewal.닫기).click()
    time.sleep(20)

    driver.find_element(By.XPATH, 변수_인증renewal.관심사_1).click()
    driver.find_element(By.XPATH, 변수_인증renewal.관심사_3).click()
    driver.find_element(By.XPATH, 변수_인증renewal.관심사_5).click()
    driver.find_element(By.XPATH, 변수_인증renewal.관심사다음버튼).click()
    # driver.find_element(By.ID, 변수_인증renewal.관심사수집닫기).click()
    # driver.find_element(By.XPATH, 변수_인증renewal.관심사수집다음에).click()



