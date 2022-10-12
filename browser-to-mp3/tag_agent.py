#Sometimes doesn't work? Rare occurence idk why. Problem is with finding //video[1] if it doesn't autoplay I think.
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

tag = "politics"
#replace tag with whatever
driver.get(f"https://www.tiktok.com/tag/{tag}?lang=en")

html = driver.find_element(By.TAG_NAME, "html")

try:
    _ = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//video[1]"))) # Wait for video to load
    elem = driver.find_element(By.XPATH, "//video[1]")
    elem.click()
    time.sleep(2)
except:
        driver.quit()


#Make a folder named audio for output
target_quantity = 10
try:
    for i in range(target_quantity):
        _ = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//video[1]"))) # Wait for video to load
        elem = driver.find_element(By.XPATH, "//video[1]")
        elem.click()
        src = elem.get_attribute("src")
        video_download(src,"audio")
        print(src)
        html.send_keys(Keys.DOWN)
        time.sleep(2) # Very arbitrary but it works at stopping duplicates. 
except Exception as e:
    print(e)
finally:
    driver.quit()
