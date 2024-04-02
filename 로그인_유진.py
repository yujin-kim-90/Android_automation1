import 변수
import 변수_로그인
import OpenCV
import pytest
import time
import os

from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver import WebElement
from selenium.webdriver.support.wait import WebDriverWait

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


# tc_id: log_03, log_04
def test_case_01(driver)->None:
    driver.find_element(By.XPATH, 변수.앱이름).click()
    time.sleep(10)
    #driver.find_element(By.ID, 변수.로그인id).click()
    #time.sleep(3)
    driver.save_screenshot(screenshotPath)
    j=1
    for i in range(5):
        for i in range(3):
            name = 'card_setting_1.png'
            driver.tap([OpenCV.Matching.detectimage(name)])
            name = 'card_setting_2.png'
            driver.tap([OpenCV.Matching.detectimage(name)])
            time.sleep(2)
        str1=driver.find_element(By.ID, 변수_로그인.간편번호불일치text_id).text
        if j <3:
            str2="간편번호가 일치하지 않습니다.("+str(j)+"/5)"
            j+=1
            assert str1 == str2
        elif 3<=j<5:
            str2="간편번호가 일치하지 않습니다.(" + str(j)+ "/5)\n5회 연속 잘못 입력 시 이용이 제한됩니다."
            j+=1
            assert str1 == str2
        else:
            str2="간편번호를 연속 5회 잘못 입력으로\n이용할 수 없습니다.\n 본인인증 후 간편번호를 \n재설정해 주세요."
            j+=1
            assert str1 == str2
        driver.find_element(By.ID, 변수_로그인.간편번호불일치_확인_id).click()

#tc_id: log_05
def test_case_02(driver)->None:
    driver.find_element(By.ID, 변수_로그인.간편번호재설정버튼_id).click()
    time.sleep(5)
    str1=driver.find_element(By.ID, 변수_로그인.간편번호재설정_본인인증_타이틀_id).text
    assert str1 == '간편번호 설정'

#tc_id: log_06
def test_case_03(driver)->None:
    driver.find_element(By.XPATH, 변수.앱이름).click()
    driver.find_element(By.ID, 변수_로그인.간편번호재설정_이름_id).send_keys(변수.고객명)
    driver.find_element(By.ID, 변수_로그인.간편번호재설정_주민등록번호_id).send_keys(변수.생년월일)
    driver.find_element(By.ID, 변수_로그인.간편번호재설정_주민뒷번호_id).click()
    time.sleep(3)
    # opencv 이용할 때, 스크린샷 한번해주고 , 파일명 선언 필요해요
    driver.save_screenshot(screenshotPath)
    name = '1_keypad_login.png'
    driver.tap([OpenCV.Matching.detectimage(name)])

    driver.find_element(By.XPATH, 변수_로그인.간편번호재설정_통신사).click()
    driver.find_element(By.ID, 변수_로그인.간편번호재설정_인증요청).click()
    time.sleep(5)
    driver.find_element(By.ID, 변수_로그인.간편번호재설정_전체동의하고인증id).click()
    time.sleep(10)
    driver.find_element(By.ID, 변수_로그인.간편번호재설정_인증번호발송_id).click()
    driver.find_element(By.ID, 변수.로그인_간편번호_인증번호입력id).send_keys("111111")
    time.sleep(10)

    for i in range(2):
        driver.save_screenshot(screenshotPath)
        for i in range(3):
            name= 'card_setting_1.png'
            driver.tap([OpenCV.Matching.detectimage(name)])
            name = 'card_setting_4.png'
            driver.tap([OpenCV.Matching.detectimage(name)])
            time.sleep(2)

    assert driver.find_element(By.ID, 변수_로그인.간편번호재설정_확인문구id).text == "간편번호가 설정되었습니다."
def test_case_04(driver)->None:
    driver.find_element(By.ID, 변수_로그인.간편번호재설정_설정확인id).click()
    time.sleep(10)
