# coding: UTF-8
from selenium import webdriver
from bs4 import BeautifulSoup
import time

casenum = 120012723000897
url = "https://servicedesk.microsoft.com/#/customer/case/" + str(casenum)

driver = webdriver.Edge()
driver.get(url)
print("Now Loading...")
time.sleep(8)

html = driver.page_source.encode('utf-8')
soup = BeautifulSoup(html, "html.parser")

titled = soup.find_all("span",class_="ng-binding")[7]
title = titled.string
print(title)

sevd = soup.a.get("title")[1]
print(len(sevd))
print(sevd)

driver.close()
print("End")
