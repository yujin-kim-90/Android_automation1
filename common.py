from 변수 import 변수
from 변수 import 변수_인증
import time
import os
import OpenCV

from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By

#여기서 현재경로 보여주고
currentPath = '%s/' % os.getcwd()
screenshotPath = currentPath + '%s-screenshot.png'

# 현재 화면의 x,y 좌표를 클릭하는 함수
def xyTouch(driver, x, y):
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(x, y)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()


def 카드인증(driver):
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

def 휴대폰인증(driver):
    driver.find_element(By.ID, 변수.로그인_이름Id).send_keys(변수.고객명)
    driver.find_element(By.ID, 변수.로그인_주민번호Id).send_keys(변수.생년월일)
    driver.find_element(By.ID, 변수.로그인_주민뒷자리Id).click()
    time.sleep(3)

    #driver.save_screenshot(OpenCV.test_screenshot(OpenCV.test_currentPath()))
    name = '1_keypad_login.png'
    driver.tap([OpenCV.Matching.detectimage(driver,name)])

    driver.find_element(By.XPATH, 변수.로그인_통신사).click()
    driver.find_element(By.ID, 변수.로그인_간편번호_인증요청).click()
    time.sleep(5)
    driver.find_element(By.ID, 변수.로그인_간편번호_전체동의하고인증id).click()
    time.sleep(10)
    driver.find_element(By.ID, 변수.인증번호_발송_id).click()
    driver.find_element(By.ID, 변수.로그인_간편번호_인증번호입력id).send_keys("111111")


def 간편번호설정(driver):
    for i in range(2):
        driver.save_screenshot(OpenCV.test_screenshot(OpenCV.test()))
        for i in range(3):
            name= 'card_setting_1.png'
            driver.tap([OpenCV.Matching.detectimage(driver, name)])
            name = 'card_setting_8.png'
            driver.tap([OpenCV.Matching.detectimage(driver, name)])
            time.sleep(2)

def 아이디비밀번호설정(driver):
    time.sleep(1)
    driver.find_element(By.XPATH,"//android.widget.ImageView[@content-desc=""1""]").click()
    time.sleep(1)
    name='r.png'
    driver.tap([OpenCV.Matching.detectimage(driver, name)])
    #driver.find_element(By.XPATH,"//android.widget.ImageView[normalize-space(@content-desc)=""q 비읍"")]").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//android.widget.ImageView[@content-desc=""2""]").click()
    name = 'r.png'
    driver.tap([OpenCV.Matching.detectimage(driver, name)])
    #driver.find_element(By.XPATH,"//android.widget.ImageView[@content-desc=""w 지읃""]").click()
    driver.find_element(By.XPATH,"//android.widget.ImageView[@content-desc=""3""]").click()
    name = 'r.png'
    driver.tap([OpenCV.Matching.detectimage(driver, name)])
    #driver.find_element(By.XPATH,"//android.widget.ImageView[@content-desc=""e 디귿""]").click()
    driver.find_element(By.XPATH,"//android.widget.ImageView[@content-desc=""4""]").click()
    name = 'r.png'
    driver.tap([OpenCV.Matching.detectimage(driver, name)])
    #driver.find_element(By.XPATH,"//android.widget.ImageView[@content-desc=""r 기역""]").click()
    # 비밀번호=["1", "q %s 비읍", "2", "w %s 지읃", "3","e %s 디귿","4","r %s 기역"]
    # for i in range(len(비밀번호)):
    #     str="//android.widget.ImageView[@content-desc="""+비밀번호[i]+"]"""
    #     driver.find_element(By.XPATH,str).click()
    time.sleep(1)
    # name = '특수문자.png'
    # driver.tap([OpenCV.Matching.detectimage(driver, name)])
    # str1="//android.widget.ImageView[@content-desc=""특수문자변경""]"
    driver.find_element(By.XPATH,"//android.widget.ImageView[@content-desc='특수문자변경']").click()
    time.sleep(1)
    # name = '특수문자.png'
    # driver.tap([OpenCV.Matching.detectimage(driver, name)])
    #driver.find_element(By.XPATH,"//android.widget.ImageView[@content-desc=""느낌표""]").click()