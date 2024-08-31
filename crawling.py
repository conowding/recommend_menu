from itertools import product
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 모든 조합을 생성
foods = ["식사", "요리", "간식"]
audience = ["혼밥", "친구", "가족", "연인", "회식"]
countries = ["한식", "중식", "일식", "양식", "아시아"]

all_combinations = list(product(foods, audience, countries))

# Selenium을 사용하여 브라우저를 열고 Chat GPT에 접속
driver = webdriver.Chrome()
driver.get("https://chat.openai.com/")  # Chat GPT의 URL로 변경하세요

# 게스트로 로그인
# 게스트로 로그인
# 게스트로 로그인
wait = WebDriverWait(driver, 10)
login_button = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div[1]/div/div/button[1]')
login_button.click()
time.sleep(5)
continue_with_google_button = driver.find_element(By.XPATH, '/html/body/div/main/section/div/div/div/div[4]/form[1]/button')
continue_with_google_button.click()
email_input = driver.find_element(By.NAME, 'identifier')
email_input.send_keys("jchuroo00@gmail.com")  # 여기에 자신의 이메일 주소를 입력하세요
email_input.send_keys(Keys.RETURN)  # 엔터 키를 누름
time.sleep(4)
password_input = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
password_input.send_keys("sks2042#")  # 여기에 자신의 비밀번호를 입력하세요
password_input.send_keys(Keys.RETURN)  # 엔터 키를 누름
time.sleep(10)
okay_lets_go_button = driver.find_element(By.XPATH, '//*[@id="radix-:rb:"]/div[2]/div/div[4]/button')
okay_lets_go_button.click()



# 모든 조합에 대해 Chat GPT에 음식 추천 요청
for combination in all_combinations:
    combination_string = f"{combination[0]} {combination[1]} {combination[2]} 음식 추천해줘"
    chat_input = driver.find_element_by_id("chat-input")
    chat_input.send_keys(combination_string)
    chat_input.send_keys(Keys.RETURN)
    
    # Chat GPT의 답변을 읽어올 수 있는 방법을 이용하여 음식 추천을 처리

# 브라우저를 종료
driver.quit()
