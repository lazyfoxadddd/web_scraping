import sys
import time 
from bs4 import BeautifulSoup
import requests
import pandas as pd


url="https://www.cricbuzz.com/"
try: 

    page=requests.get(url)

except Exception as e:
    error_type, error_obj, error_info = sys.exc_info()
    print('ERROR FOR LINK: ', url)
    print(error_type, 'Line:', error_info.tb_lineno)


time.sleep(2)

soup=BeautifulSoup(page.text, "html.parser")
links=soup.find_all('h2',attrs={"class":"big-crd-hdln"})


for link in links:
    print(link.text)
    print('\n')