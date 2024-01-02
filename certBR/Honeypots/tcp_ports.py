import requests
from bs4 import BeautifulSoup
import csv
import os

"""
the site that has been collected : https://stats.cert.br/honeypots/
"""




class TCP:
    def __init__(self):
        self.url = 'https://stats.cert.br/data/honeypots/tcp_ports_ts.txt'

    print(os.getcwd())
    def mkdir(self):   
        
        dir = os.getcwd() + '\\certBR\\Honeypots'
        os.chdir(dir)

        folder_name = 'tcp-udp'
 
        try:
            os.mkdir(folder_name)
            print('Folder created')
            os.chdir(dir + '\\tcp-udp')

        except FileExistsError:
            print('Folder already exist')
            os.chdir(dir + '\\tcp-udp')


    def request(self):
        req = requests.get(self.url)
        bs4_obj = BeautifulSoup(req.content, 'html.parser')
        
        return bs4_obj

    def parsing(self):


        a = []
        bs4 = self.request()
        for c in bs4:
            bs4 = c.text.replace('#', '')
            bs4 = bs4.split('\n')
            for value in bs4:
                bs4 = value.split(';')
                a.append(bs4)

        del a[0]
        del a[-1]
        del a[-1]
        head = a[0]
        del a[0]

        a.reverse()

        del head[1]
        data_clear = [head]

        for value in a:
            del value[1]
            data_clear.append(value)

            if value[0] == '2023-01-01':
                break

        return data_clear

    def main(self):
        


        self.mkdir()
        ports_tcp = self.parsing()

        with open(f'tcp_ports.csv','w', newline='') as f:
            writer = csv.writer(f)
            for data in ports_tcp:
                writer.writerow(data)

        print('file created')



a = TCP()

a.main()

