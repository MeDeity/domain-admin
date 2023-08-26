import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select
import win32com.client

def initDriver():
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-data-dir=C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
    # options.add_experimental_option("debuggerAddress", "localhost:10000") 
    # options.add_argument("--headless")  
    options.add_argument('--ignore-certificate-errors') 
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 30) 
    return driver,wait

# how to use : wait_for_visibility(driver, By.ID, "my-element-id")
def wait_for_visibility(driver, by, value, timeout=10):
    wait = WebDriverWait(driver, timeout)
    element = wait.until(EC.visibility_of_element_located((by, value)))
    return element

# 是否可点击
def wait_for_clickable(driver, by, value, timeout=10):
    wait = WebDriverWait(driver, timeout)
    element = wait.until(EC.element_to_be_clickable((by, value)))
    return element

def wait_for_input(driver, by, value, input, timeout=10):
    wait = WebDriverWait(driver, timeout)
    element = wait.until(EC.element_to_be_clickable((by, value)))
    if element:
        element.send_keys(input)
    return element

#等待并点击
def wait_for_click(driver, by, value, timeout=10):
    wait = WebDriverWait(driver, timeout)
    element = wait.until(EC.element_to_be_clickable((by, value)))
    if element:
        element.click()
    return element

# 是否可点击
def wait_for_all_elements(driver, by, value, timeout=10):
    wait = WebDriverWait(driver, timeout)
    elements = wait.until(EC.presence_of_all_elements_located((by, value)))
    return elements




def handle():
    # toRegister()
    # userDetail()
    # uploadAvatar()
    start()

    # element = wait_for_visibility(driver,By.CSS_SELECTOR,"#changeList > tbody > gr-change-list-item:nth-child(20) > td.cell.subject.style-scope.gr-change-list-item")
    # title = element.text
    # print(title)


def process():
    # open website
    driver,wait = initDriver()
    driver.get("https://badoo.com/")    

def register():
    driver,wait = initDriver()
    driver.get("https://badoo.com/")    
    wait_for_input(driver,By.CSS_SELECTOR,"#login","langrenbule@gmail.com")
    time.sleep(3)
    wait_for_click(driver,By.CSS_SELECTOR,"#gdpr_no")    
    time.sleep(3)
    wait_for_input(driver,By.CSS_SELECTOR,"#main > div > div.homepage-promo__in > div > div.sign-flow.sign-flow--1.sign-flow--skip.js-signup-flow.sign-flow--2 > div.sign-flow__steps.js-signup-steps-wrapper.js-core-events-container > div > div > div > form > div:nth-child(3) > div.new-form__field > div > input","Ab135790")
    time.sleep(3)
    wait_for_click(driver,By.CSS_SELECTOR,"#main > div > div.homepage-promo__in > div > div.sign-flow.sign-flow--1.sign-flow--skip.js-signup-flow.sign-flow--2 > div.sign-flow__steps.js-signup-steps-wrapper.js-core-events-container > div > div > div > form > div.new-form__actions > button")
    time.sleep(600)

def toRegister():
    driver,wait = initDriver()
    driver.get("https://eu1.badoo.com/signup/?f=top")     
    # wait_for_click(driver,By.CSS_SELECTOR,"#header > div > div.header__sign-in > div > div > a")   
    time.sleep(3)
    wait_for_input(driver,By.CSS_SELECTOR,"#login","medeity@gmail.com")
    time.sleep(3)
    wait_for_click(driver,By.CSS_SELECTOR,"#gdpr_no")   
    time.sleep(3)
    wait_for_input(driver,By.CSS_SELECTOR,"#main > section > div > div > div.sign-page__form.js-core-events-container > form > div:nth-child(3) > div.new-form__field > div > input","Ab135790")
    time.sleep(3)
    wait_for_click(driver,By.CSS_SELECTOR,"#main > section > div > div > div.sign-page__form.js-core-events-container > form > div.new-form__actions > button")   
    time.sleep(3600)

def userDetail():
    driver,wait = initDriver()
    driver.get("https://badoo.com/")
    # time.sleep(3600)
    wait_for_input(driver,By.CSS_SELECTOR,"#first_name","medeity")

    day = wait_for_click(driver,By.CSS_SELECTOR,"#simple-page > div.page__content > section > div > div > div > form > div:nth-child(2) > div.new-form__field.js-date-field > div > div.date-field__item.date-field__item--day > div")
    if day:
        wait_for_click(driver,By.XPATH,'//*[@id="simple-page"]/div[3]/section/div/div/div/form/div[2]/div[2]/div/div[1]/div/div[3]/div/div/div[1]/ul/li[1]')        
    
    month = wait_for_click(driver,By.CSS_SELECTOR,"#simple-page > div.page__content > section > div > div > div > form > div:nth-child(2) > div.new-form__field.js-date-field > div > div.date-field__item.date-field__item--month > div")
    if month:
        wait_for_click(driver,By.XPATH,'//*[@id="simple-page"]/div[3]/section/div/div/div/form/div[2]/div[2]/div/div[2]/div/div[3]/div/div/div[1]/ul/li[1]')
    
    year = wait_for_click(driver,By.CSS_SELECTOR,"#simple-page > div.page__content > section > div > div > div > form > div:nth-child(2) > div.new-form__field.js-date-field > div > div.date-field__item.date-field__item--year > div")
    if year:
        wait_for_click(driver,By.XPATH,'//*[@id="simple-page"]/div[3]/section/div/div/div/form/div[2]/div[2]/div/div[3]/div/div[3]/div/div/div[1]/ul/li[1]/div')        

    city = wait_for_click(driver,By.CSS_SELECTOR,"#location_field")
    if year:
        wait_for_click(driver,By.XPATH,'//*[@id="data-list-location-list"]/li[11]')

    wait_for_click(driver,By.CSS_SELECTOR,"#female")
    wait_for_click(driver,By.CSS_SELECTOR,"#simple-page > div.page__content > section > div > div > div > form > div.new-form__actions > button")

    wait_for_input(driver,By.XPATH,'//*[@id="simple-page"]/div[2]/section/div[1]/div[2]/div[1]/div/div[2]/div/div',"C:\\Users\\Administrator\\Desktop\\1.jpg")
    time.sleep(3600)

def uploadAvatar():
    driver,wait = initDriver()
    driver.get("https://badoo.com/")
    
    #继续
    wait_for_click(driver,By.CSS_SELECTOR,"#simple-page > div.page__content > section > div.simple-promo__content > div.simple-promo__actions > button")

    # file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    # file_input.send_keys("C:\\Users\\Administrator\\Desktop\\1.jpg")
    # wait_for_input(driver,By.XPATH,'//*[@id="simple-page"]/div[2]/section/div[1]/div[2]/div[1]/div/div[2]/div/div',"C:\\Users\\Administrator\\Desktop\\1.jpg")
    time.sleep(3600)    

def start():
    driver,wait = initDriver()
    driver.get("https://badoo.com/")
    for i in range(1):
        print("....")
        wait_for_click(driver,By.CSS_SELECTOR,'#mm_cc > div.encounters-card__inner > section > div > div.big-photo__actions.js-profile-actions-container.js-core-events-container > div > div.encounters-actions__main-items.js-profile-header-buttons > div.encounters-actions__item.encounters-actions__item--yes > button')
        time.sleep(3.5)   
    element = wait_for_visibility(driver,By.CSS_SELECTOR,"#tabbar > nav > a:nth-child(4) > div.sidebar-menu__item-mark > span")     
    if element:
        numberStr = element.text or '0'
        number = int(numberStr)
        print("element:",number)
        # 准备聊天
        wait_for_click(driver,By.CSS_SELECTOR,'//*[@id="tabbar"]/nav/a[3]')
        

    
        

    time.sleep(3600)
    






def lookEmail():
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6)
    messages = inbox.Items
    for message in messages:
        print(message.Subject)
# hotmail
# oneguhfenyc@hotmail.com
# aBBHSz37
def loginEmail():
    driver,wait = initDriver()
    driver.get("https://outlook.live.com/owa/")
    wait_for_click(driver,By.CSS_SELECTOR,"body > header > div > aside > div > nav > ul > li:nth-child(2) > a")
    email = wait_for_visibility(driver,By.CSS_SELECTOR,"#i0116")
    if email is None:
        return
    email.send_keys("oneguhfenyc@hotmail.com")

    print("账号输入")
    emailNext = wait_for_click(driver,By.CSS_SELECTOR,"#idSIButton9")
    if emailNext is None:
        return

    pwd = wait_for_visibility(driver,By.CSS_SELECTOR,"#i0118")
    if pwd is None:
        return
    pwd.send_keys("aBBHSz37")
    print("密码输入")
    pwdNext = wait_for_click(driver,By.CSS_SELECTOR,"#idSIButton9")
    if pwdNext is None:
        return
    print("等待跳过")
    # wait_for_click(driver,By.CSS_SELECTOR,"#iShowSkip")
    # wait_for_click(driver,By.CSS_SELECTOR,"#idBtn_Back")

def decodeEmail():    
    driver,wait = initDriver()
    driver.get("https://outlook.live.com/owa/")

    wait_for_click(driver,By.CSS_SELECTOR,"#Pivot79-Tab1 > span > div")
    time.sleep(200)
