import requests
import bs4
import csv
import os

"""
the page that i am collecting is : https://stats.cert.br/phishing/
"""

class IoC:
    def __init__(self) -> None:
        self.url = 'https://stats.cert.br/data/phishing/2023/summary.txt?_=1695439898627'
        os.chdir(os.getcwd() + '\\certBR\\phising_page')
    
    def mkdir(self):
        try:
            os.mkdir('Phising')
            print("Folder created")
        except FileExistsError:
            print('folder already exist')

    def request(self):
        req = requests.get(self.url)
        bs = bs4.BeautifulSoup(req.content,'html.parser')
        return bs
    
    def parsing(self, bs4_content: bs4.BeautifulSoup):
        clear = []
        bs = bs4_content.text.split('\n')
        del bs[0]
        del bs[0]
        del bs[1]
        del bs[-1]
        del bs[-1]
        del bs[-1]
        
        for value in bs:
            bs = value.replace('#', '')
            bs = bs.replace('\t','' )
            bs = bs.replace('\n', '')
            bs = bs.split('\n')
        
            for v in bs:
                bs = v.strip().split(':')
            clear.append(bs)

        del clear[0]
    
        return clear
        
    def main(self):
        self.mkdir()
        
        request_content = self.request()
        data_to_csv = self.parsing(request_content)

        with open(f'Phising\\phising.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            for line in data_to_csv:
                writer.writerow(line)
        





IOC = IoC()
IOC.main()
