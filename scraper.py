#%%
from selenium import webdriver
browser = webdriver.Firefox()

# %%
url = 'https://en.wikipedia.org/wiki/Nicolas_Cage_filmography'
browser.get(url)
sleep(5)
browser.close()
# %%
