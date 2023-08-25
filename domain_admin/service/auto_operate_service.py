import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service


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


def handle():
    driver,wait = initDriver()
    driver.get("https://www.baidu.com")


    # element = wait_for_visibility(driver,By.CSS_SELECTOR,"#changeList > tbody > gr-change-list-item:nth-child(20) > td.cell.subject.style-scope.gr-change-list-item")
    # title = element.text
    # print(title)