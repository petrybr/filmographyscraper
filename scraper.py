import time
import pandas as pd
from selenium import webdriver
browser = webdriver.Firefox()
url = 'https://en.wikipedia.org/wiki/Nicolas_Cage_filmography'
browser.get(url)
time.sleep(5)
filmography = browser.find_element_by_xpath('/html/body/div[3]/div[3]/div[5]/div[1]/table[1]')
df = pd.read_html('<table>' + filmography.get_attribute('innerHTML') + '</table>')[0]
df.to_csv('nicolas_cages_filmography.csv', sep=';', index=False)
browser.quit()