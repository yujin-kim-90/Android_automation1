#인증 > 아이디

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
    driver.find_element(By.XPATH, 변수.앱이름).click()
    time.sleep(10)
    driver.find_element(By.ID, 변수.시작하기_로그인Id).click()
    time.sleep(10)

    driver.find_element(By.ID, 변수_인증.다른로그인방법id).click()
    time.sleep(3)
    driver.find_element(By.XPATH, 변수_인증.로그인방법_아이디).click()
    time.sleep(3)
    driver.find_element(By.ID, 변수_인증.아이디비번설정id).click()
    time.sleep(3)
    str1=driver.find_element(By.ID, 변수_인증.간편번호설정문구확인id).text

    assert str1=="본인 인증"

#tc_id: log_35
def test_case_02(driver)->None:
    driver.find_element(By.XPATH, 변수.앱이름).click()
    time.sleep(10)
    for i in range(len(변수.카드번호)):
        #driver.find_element(By.XPATH, 변수_인증.카드번호입력id).click()
        str="//android.widget.ImageView[@content-desc="""+변수.카드번호[i]+"]"""
        driver.find_element(By.XPATH,str).click()


    driver.find_element(By.ID, 변수_인증.유효기간월id).send_keys("01")
    driver.find_element(By.ID, 변수_인증.유효기간년도id).send_keys("25")

    for i in range(len(변수.카드cvc)):
        #driver.find_element(By.XPATH, 변수_인증.카드번호입력id).click()
        str="//android.widget.ImageView[@content-desc="""+변수.카드cvc[i]+"]"""
        driver.find_element(By.XPATH,str).click()

    driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="1"]').click()
    driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="2"]').click()

    time.sleep(10)

    str1=driver.find_element(By.ID, 변수_인증.간편번호설정문구확인id).text
    assert str1=="아이디/비밀번호 입력"

#tc_id: log_36,38
def test_case_03(driver)->None:
    #driver.find_element(By.ID, 변수_인증.아이디비번설정x버튼id).click()
    driver.find_element(By.XPATH, 변수.앱이름).click()
    time.sleep(10)
    driver.find_element(By.ID, 변수_인증.아이디비번설정id).click()
    time.sleep(5)
    driver.find_element(By.XPATH, 변수_인증.본인인증휴대폰).click()
    time.sleep(5)
    driver.find_element(By.ID, 변수.로그인_이름Id).send_keys(변수.고객명)
    driver.find_element(By.ID, 변수.로그인_주민번호Id).send_keys(변수.생년월일)
    driver.find_element(By.ID, 변수.로그인_주민뒷자리Id).click()
    time.sleep(3)
    # opencv 이용할 때, 스크린샷 한번해주고 , 파일명 선언 필요해요
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

    str1=driver.find_element(By.ID, 변수_인증.간편번호설정문구확인id).text
    assert str1=="아이디/비밀번호 입력"





