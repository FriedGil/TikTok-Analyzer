from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from download import video_download
import time 

options = webdriver.FirefoxOptions()
options.add_argument("--ignore-ssl-errors=yes")
options.add_argument("--ignore-certificate-errors")
driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub", options=options
)
try: driver.get("https://www.tiktok.com/foryou")
except: print("This shouldn't happen")


try: html = driver.find_element(By.TAG_NAME, "html")
except: print("This shouldn't happen either")

try:
    for i in range(500):
        _ = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//video[1]"))) # Wait for video to load
        elem = driver.find_element(By.XPATH, "//video[1]")
        src = elem.get_attribute("src")
        video_download(src)
        print(src)
        html.send_keys(Keys.DOWN)
        time.sleep(2) # Very arbitrary but it works at stopping duplicates. 
except Exception as e:
    print(e)
finally:
    driver.quit()
