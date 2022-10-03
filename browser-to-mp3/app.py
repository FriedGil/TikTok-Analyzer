from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.FirefoxOptions()
options.add_argument("--ignore-ssl-errors=yes")
options.add_argument("--ignore-certificate-errors")
driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub", options=options
)
driver.get("https://www.tiktok.com/foryou")

wait = WebDriverWait(driver, 10)
html = driver.find_element(By.TAG_NAME, "html")
try:
    element = wait.until(EC.presence_of_element_located((By.XPATH, "//video[1]")))
    elem = driver.find_element(By.XPATH, "//video[1]").get_attribute("src")
    print(elem)
    videos = {}
    for i in range(5):
        html.send_keys(Keys.DOWN)
        driver.implicitly_wait(1)
        elem = driver.find_element(By.XPATH, "//video[1]").get_attribute("src")
        print(elem)
    
    driver.quit()
except Exception as e:
    print(e)
    driver.quit()
