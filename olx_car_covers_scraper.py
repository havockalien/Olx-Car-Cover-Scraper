
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import csv

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options)
driver.get("https://www.olx.in/items/q-car-cover")

time.sleep(5)

for _ in range(3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

items = driver.find_elements(By.CSS_SELECTOR, "li.EIR5N")
data = []

for item in items:
    try:
        title = item.find_element(By.CSS_SELECTOR, "span._2tW1I").text
        price = item.find_element(By.CSS_SELECTOR, "span._89yzn").text
        location = item.find_element(By.CSS_SELECTOR, "span._2Fxz3").text
        data.append([title, price, location])
    except:
        pass

with open("olx_car_covers.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price", "Location"])
    writer.writerows(data)

driver.quit()
print("done")
