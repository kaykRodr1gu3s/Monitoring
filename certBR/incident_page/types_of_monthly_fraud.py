import requests
from bs4 import BeautifulSoup
import os
import csv

"""the page that i am collecting is : https://stats.cert.br/incidentes/"""

class monthly_fraud():
    def __init__(self):
        self.url = 'https://stats.cert.br/data/incidentes/2023/tipos-incidente-mensal.txt?_=1695404587931'


    def mkdir(self):
    
        dir_name = os.getcwd() + '\\certBR\\incident_page'
        folder_name = 'Incident'
        folder_path = os.path.join(dir_name, folder_name)

        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
            print('Folder created')
        else:
            print('Folder already exist')

        current = os.getcwd() +'\\certBR\\incident_page\\Incident'

        return current


    def request(self):

        req = requests.get(self.url)
        bs_obj = BeautifulSoup(req.content, 'html.parser')
        bs_obj = bs_obj.text.split('\n')
        
        return bs_obj
    

    def parsing(self):
        bs = self.request()
        clear = []

        for c in bs:
            bs = c.replace('#', '')
            bs = bs.replace('num', 'quantity')
            bs = bs.replace('%', 'percentage')
            bs = bs.replace('Mês', 'month')
            bs = bs.replace('Invasão', 'invasion')
            bs = bs.split()
            clear.append(bs)

        del clear[0]

        return clear


    def main(self):
        with open(f'{self.mkdir()}\\types_of_montly_fraud.csv','w', newline='') as f:
            writer  = csv.writer(f)
            for line in self.parsing():
                writer.writerow(line)


fraud = monthly_fraud()
fraud.main()