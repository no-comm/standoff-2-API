from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import time
import requests

def account(id: str):
    chrome_options = Options()
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    avatar = ""
    name = ""
    driver.get('https://store.standoff2.com/?search')
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#boom > div > div > div > div.MuiBox-root.jss9 > div.MuiFormControl-root.MuiTextField-root.sc-AxhUy.fxWvvr.MuiFormControl-fullWidth > div > input')))
    driver.find_element(By.CSS_SELECTOR, '#boom > div > div > div > div.MuiBox-root.jss9 > div.MuiFormControl-root.MuiTextField-root.sc-AxhUy.fxWvvr.MuiFormControl-fullWidth > div > input').send_keys(id)
    driver.find_element(By.CSS_SELECTOR, "#boom > div > div > div > div.MuiBox-root.jss9 > div.MuiBox-root.jss14 > button > span").click()
    WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "#boom > div > div > div > div.MuiBox-root.jss60.sc-AxiKw.eSbheu.AccountLine_container > div > div.MuiBox-root.jss62 > div.MuiBox-root.jss64")))
    time.sleep(1)
    try:
        driver.get(f"https://store.standoff2.com/ru/profile/{id}")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#root > div > div.MuiPaper-root.sc-Axmtr.sc-AxmLO.cAKCgh.PageContent-root.MuiPaper-elevation1.MuiPaper-rounded > div > div.MuiBox-root.jss7.sc-AxiKw.eSbheu.AccountLine_container > div > div.MuiBox-root.jss9 > div.MuiBox-root.jss11")))
        try:
            avatar = driver.find_element(By.CLASS_NAME, "MuiAvatar-img").get_attribute('src')
        except:
            pass
        name = driver.find_element(By.CSS_SELECTOR, "#root > div > div.MuiPaper-root.sc-Axmtr.sc-AxmLO.cAKCgh.PageContent-root.MuiPaper-elevation1.MuiPaper-rounded > div > div.MuiBox-root.jss7.sc-AxiKw.eSbheu.AccountLine_container > div > div.MuiBox-root.jss9 > div.MuiBox-root.jss11").text
    except Exception as ex:print(ex)
    driver.quit()
    return name, avatar
def avatar(url: str):
    f=open(r'gg.webp', "wb")
    ufr = requests.get(url)
    f.write(ufr.content)
    f.close()