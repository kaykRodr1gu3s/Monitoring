import requests
import os
import csv
from bs4 import BeautifulSoup





"""the page that i am collecting is : https://stats.cert.br/ioc/"""





class IoC:
    def __init__(self):
        self.url = 'https://stats.cert.br/data/ioc/summary_stats.txt?_=1695604816610'
        


    def mkdir(self):
        current_dir = os.getcwd() + '\\certBR\\IoC'    
        os.chdir(current_dir)
        print(os.getcwd())
        try: 
            os.mkdir('IOC')
            os.chdir(current_dir + '\\IOC')
            print('Folder created')

        except FileExistsError:
            os.chdir(current_dir + '\\IOC')
            print('Folder already exist')

    def request(self):
        req = requests.get(self.url)
        bs4 = BeautifulSoup(req.content, 'html.parser')
        bs4 = bs4.text.split('\n')

        return bs4
    
    def parsing(self):
        bs4 = self.request()
        head = [' ', 'Proxy 4145','TCP', 'Proxy 5678', 'TCP']

        data_clear = [head]
        for c in bs4:
            bs4 = c.split('|')
            data_clear.append(bs4)

        del data_clear[-1]

        data_clear[1][1] = "ASN"
        data_clear[1][2] = "IP"
        data_clear[1][3] = "ASN"
        data_clear[1][4] = "IP"        
        
        return data_clear

    def main(self):
        self.mkdir()
        with open(f'IoC.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            for c in self.parsing():
                writer.writerow(c)


ioc = IoC()
ioc.main()