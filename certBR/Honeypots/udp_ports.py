import requests
from bs4 import BeautifulSoup
import csv
import os



"""
the site that has been collected : https://stats.cert.br/honeypots/
"""



class UDP:
    def __init__(self):
        self.url = 'https://stats.cert.br/data/honeypots/udp_ports_ts.txt'

    def mkdir(self):
        current_dir = os.getcwd() + '\\certBR\\Honeypots'    
        os.chdir(current_dir)
 
        try:
            os.mkdir('tcp-udp')
            os.chdir(current_dir + '\\tcp-udp')

        except FileExistsError:
            print('Folder already exist')
            os.chdir(current_dir + '\\tcp-udp')

    def request(self):
        req = requests.get(self.url)


        bs4_obj = BeautifulSoup(req.content, 'html.parser')
        
        return bs4_obj


    def parsing(self):

        requests_content = self.request()
        datas_clear = []

        for data_obj in requests_content:
            bs4 = data_obj.text.replace('#', '')
            bs4 = bs4.split('\n')

            for value in bs4:
                bs4 = value.split(';')
                datas_clear.append(bs4)

        del datas_clear[0]
        del datas_clear[-1]
        del datas_clear[-1]
        head = datas_clear[0]
        del datas_clear[0]

        datas_clear.reverse()

        del head[1]
        data_clear = [head]

        for value in datas_clear:
            del value[1]
            data_clear.append(value)

            if value[0] == '2023-01-01':
                break

        return data_clear
    
    
    def main(self):
    
        self.mkdir()
        data_parsed = self.parsing()

        with open(f'udp_ports.csv','w', newline='') as f:
            writer = csv.writer(f)
            for c in data_parsed:
                writer.writerow(c)
        print('File created')

udp = UDP()
udp.main()