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

#tc_id: log_20
def test_case_01(driver)->None:
    driver.find_element(By.XPATH, 변수.앱이름).click()
    time.sleep(10)
    driver.find_element(By.ID, 변수.시작하기_로그인Id).click()
    time.sleep(10)
    driver.find_element(By.ID, 변수.로그인id).click()
    time.sleep(3)

    assert driver.find_element(By.ID, 변수_인증.간편번호설정문구확인id).text == "간편번호 설정"

#tc_id: log_22
def test_case_02(driver)->None:
    driver.find_element(By.ID, 변수.로그인_이름Id).send_keys(변수.고객명)
    driver.find_element(By.ID, 변수.로그인_주민번호Id).send_keys(변수.생년월일)
    driver.find_element(By.ID, 변수.로그인_주민뒷자리Id).click()
    time.sleep(3)

    driver.save_screenshot(screenshotPath)
    name = '1_keypad_login.png'
    driver.tap([OpenCV.Matching.detectimage(name)])

    driver.find_element(By.XPATH, 변수.로그인_통신사).click()
    driver.find_element(By.ID, 변수.로그인_간편번호_인증요청).click()
    time.sleep(5)
    driver.find_element(By.ID, 변수.로그인_간편번호_전체동의하고인증id).click()
    time.sleep(10)
    driver.find_element(By.ID, 변수.인증번호_발송_id).click()
    driver.find_element(By.ID, 변수.로그인_간편번호_인증번호입력id).send_keys("111111")
    time.sleep(10)
    assert driver.find_element(By.ID, 변수_인증.간편번호설정문구확인id).text == "간편번호 설정"

#tc_id: log_23
def test_case_03(driver)->None:
    for i in range(2):
        driver.save_screenshot(screenshotPath)
        for i in range(3):
            name= 'card_setting_1.png'
            driver.tap([OpenCV.Matching.detectimage(name)])
            name = 'card_setting_4.png'
            driver.tap([OpenCV.Matching.detectimage(name)])
            time.sleep(2)

    driver.find_element(By.ID, 변수.지문등록시트_x버튼).click()
    time.sleep(10)

    driver.save_screenshot(screenshotPath)
    name='card_setting_1.png'
    driver.tap([OpenCV.Matching.detectimage(name)])
    name = 'card_setting_2.png'
    driver.tap([OpenCV.Matching.detectimage(name)])
    time.sleep(10)

    driver.find_element(By.ID, 변수_인증.ars인증요청id).click()

    time.sleep(10)

    driver.find_element(By.ID, 변수_인증.로카페이반팝업종료id).click()
    str1=driver.find_element(By.XPATH, 변수_인증.로카페이타이틀확인).text

    assert str1=="로카페이"

def test_case_04(driver)->None:
    driver.find_element(By.ID, 변수_인증.로카페이메인종료).click()
    str1=driver.find_element(By.XPATH, 변수_인증.홈확인).text

    assert str1=="홈"







