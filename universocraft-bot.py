from undetected_chromedriver import Chrome
from selenium.webdriver import ChromeOptions
import time

options = ChromeOptions()
driver = Chrome(options=options)

driver.get("https://stats.universocraft.com/jugador/[player-name]") # Edit "player-name"

time.sleep(10)

html = driver.page_source

print(html)
driver.quit()
