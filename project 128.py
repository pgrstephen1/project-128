from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Edge("C:/Whitehat_jr/PRO-127-130/msedgedriver.exe")
browser.get(START_URL)
soup = BeautifulSoup(browser.page_source, "html.parser")

star_table = soup.find_all('table')

table_rows = star_table[7].find_all('tr')

new_planets_data = []


for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    new_planets_data.append(row)
Star_names = []
Distance = []
Mass = []
Radius = []


for i in range(1, len(new_planets_data)):
    Star_names.append(new_planets_data[i][0])
    Distance.append(new_planets_data[i][5])
    Mass.append(new_planets_data[i][7])
    Radius.append(new_planets_data[i][8])

df2 = pd.DataFrame(list(zip(Star_names, Distance, Mass, Radius)), 
columns=['Star_name', 'Distance', 'Mass', 'Radius']) 
print(df2) 
df2.to_csv('field_brown_dwarfs.csv')
