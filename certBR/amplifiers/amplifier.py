
import requests
from bs4 import BeautifulSoup
import csv
import os

"""the page that i am collecting is : https://stats.cert.br/amplificadores/"""

class amplifiers:
    def __init__(self) -> None:
        self.url = 'https://stats.cert.br/data/amplificadores/summary_stats.txt?_=1695595795758'


    def mkdir(self):
        dir_name = os.getcwd() + '\\certBR\\amplifiers'
        os.chdir(dir_name)
      
        folder_name = 'amplifiers'
        folder_path = os.path.join(dir_name, folder_name)
 
 
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
            print('Folder created')
 

 
        else:
            print('Folder already exist')

        current = os.getcwd() +'\\amplifiers'
        
        return current



    def request(self):
        data_clear = []
        req = requests.get(self.url)
        bs4 = BeautifulSoup(req.content, 'html.parser')


        bs4 = bs4.text
        bs4 = bs4.split('\n')



        del bs4[-1]

        for c in bs4:
            bs4 = c.split('|')

            data_clear.append(bs4)

        return data_clear

amplifier = amplifiers()
with open(f'{amplifier.mkdir()}\\amplifiers.csv', 'w', newline='') as f:
    writter = csv.writer(f)
    for c in amplifier.request():
        writter.writerow(c)


