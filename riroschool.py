from selenium import webdriver
import time
import pyautogui
from datetime import datetime

print("본 프로그램은 리로스쿨 수강신청을 위한 매크로 프로그램입니다,")
print("본 프로그램은 개발연습용으로 개발되었으며, 누구나 깃헙에서 해당 소스를 확인할 수 있습니다.")
print("본 소프트웨어는 개발자인 신재욱(YellJ)에 의해 제작되었으며, 개발 연습을 위해 제작되었습니다.")
print("해당 소프트웨어를 이용해 생기는 모든 책임은 모두 사용자에게 있으며, 개발자는 어떠한 책임도 지지 않습니다.")
print("Windows10 Pro, 신재욱(YellJ), 2018-8-22")
print("----------------------------------------------------------------------------------------------------")
print("#주의사항#")
print("1. 해당 작업을 하는 컴퓨터는 반드시 다른 작업을 같이해서는 안됩니다.")
print("2. 본 프로그램은 자동으로 엔터 등 각종 키를 누릅니다. 건드리시면 제대로 동작하지 않습니다.")
print("3. 본 소프트웨어를 사용하기 위해선 chromedriver.exe 파일과 크롬 브라우저가 필요합니다.")
print("----------------------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------")
rirolink=input("학교의 리로스쿨 url을 적어주세요! 대신고 학생은 그냥 1만 입력하면되요! (예:https://dshs.riroschool.kr):\n")
if rirolink=='1':
    rirolink='https://dshs.riroschool.kr'
id=input("리로스쿨 아이디 : ")
if id=="":
    print("아무것도 입력하지 않으셨어요!")
    exit()
pw=input("리로스쿨 비밀번호 : ")
if pw=="":
    print("아무것도 입력하지 않으셨어요!")
    exit()
idlist=list(id)
pwlist=list(pw)

number=int(input("몇개의 수강신청을 하시겠습니까? : "))
if number<1:
    print("장난은 ㄴㄴ")
    exit()
listvar=number-1
url=[]
for i in range(number):
    ask=input("수강신청하고자 하는 URL을 입력하세요(예: https://dshs.riroschool.kr/lecture.php?club=index&action=view&db=1701&page=1&cate=17&cls=&sort=rate&uid=2262&inum=0&key=&key2=&s1=&s2=&s3=) : \n")
    url.append(ask)
    print("현재 입력하신 URL > "+str(url)+"\n")
print("로딩중..")
time.sleep(2)
playtime=input("작동할 시간을 입력하세요 3:01 -> 03:01 으로 입력")

driver=webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(1)

driver.get(rirolink+"/user.php")
driver.find_element_by_name('mid').click()
pyautogui.press(idlist)

driver.find_element_by_name("mpass").click()
pyautogui.press(pwlist)
driver.find_element_by_xpath('//*[@id="main_content"]/form/div/input[3]').click()

driver.get(rirolink+'/lecture.php?action=device&db=1701&cate=17&confirm='+id)

while True:
    now=datetime.now()
    hour=now.hour
    minute=now.minute
    if hour<10:
        hour='0'+str(hour)
    if minute<10:
        minute='0'+str(minute)

    nowtime=str(hour)+':'+str(minute)
    print(str(nowtime)+' [이 시각이 설정된 시각과 일치하면 실행합니다.]')
    if playtime==nowtime:
        break
for go in url:
    driver.get(go)
    driver.find_element_by_css_selector('#button').click()
    pyautogui.press('enter')
    time.sleep(0.5)
    print("성공! 다음 수강신청을 합니다!")