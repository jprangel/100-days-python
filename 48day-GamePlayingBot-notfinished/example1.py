from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

BROWSER = "/Users/jessica.rangel/chromedriver/chromedriver"
URL="https://python.org"

svc = Service(BROWSER)
driver= webdriver.Chrome(service=svc)
driver.set_window_size(400,600)
driver.get(URL)


events_time = driver.find_elements(By.CSS_SELECTOR, '.event-widget li time')
events_title = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')
events = {}
for n in range(len(events_time)):
    events[n] = { 
        'time': events_time[n].text,
        'name': events_title[n].text
    }
print(events)
driver.quit()