from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


options = webdriver.FirefoxOptions()
options.add_argument("--ignore-ssl-errors=yes")
options.add_argument("--ignore-certificate-errors")
driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub", options=options
)
driver.get("https://www.tiktok.com/foryou")



try:
    driver.get("https://www.tiktok.com/foryou")
    html = driver.find_element(By.TAG_NAME, "html")
    while True:
        sleep(1)

finally:
    driver.quit()
