import requests
from bs4 import BeautifulSoup
import os
import csv

"""the page that i am collecting is : https://stats.cert.br/incidentes/"""



class top_ports():
    def __init__(self):
        self.url = 'https://stats.cert.br/data/incidentes/2023/top-portas.txt'


    def mkdir(self):

        dir_name = os.getcwd() + '\\certBR\\incident_page'
        os.chdir(dir_name)
        print(os.getcwd())

        folder_name = 'Incident'

        try:

            os.mkdir(folder_name)
            print('Folder created')
            os.chdir(dir_name + '\\Incident')
            print('folder created')

        except FileExistsError:

            print('Folder already exist')
            os.chdir(dir_name + '\\Incident')

            
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
            bs = bs.replace('tipo', 'kind')
            bs = bs.replace('porta', 'port')
            bs = bs.split()
            clear.append(bs)

        del clear[0]

        return  clear

    def main(self):
        self.mkdir()
        data_to_csv = self.parsing()
        with open(f'top_ports.csv','w', newline='') as f:
            writer  = csv.writer(f)
            for line in data_to_csv:
                writer.writerow(line) 


a = top_ports()
a.main()









