from undetected_chromedriver import Chrome
from selenium.webdriver import ChromeOptions
import time

options = ChromeOptions()
driver = Chrome(options=options)

driver.get("https://stats.universocraft.com/jugador/unicz")

time.sleep(10)

html = driver.page_source

print(html)
driver.quit()
