import requests
import bs4
import csv
import os

"""
the site that has been collected : https://stats.cert.br/spam/
"""


class agruped_by_ip:
    def __init__(self) -> None:
        self.url = 'https://stats.cert.br/data/spam/2023/acumulado-ip.txt'
        os.chdir(os.getcwd() + '\\certBR\\spam')


    def mkdir(self):
        try:
            os.mkdir('Spam report')

        except FileExistsError:
            print('file already exist')
    
    def request(self):
        req = requests.get(self.url)
        bs = bs4.BeautifulSoup(req.content, 'html.parser')
        
        return bs
        
    def parsing(self, bs4_content: bs4.BeautifulSoup):
        bs = bs4_content
        head = ['position', 'quantity', 'IP_Address']
        data_clear = [head]

        bs = bs.text.replace('#','')
        bs = bs.split('\n')

        del bs[0]
        del bs[-1]

        for value in bs:
            bs = value.split()
            data_clear.append(bs)

        return data_clear

    def main(self):
        self.mkdir()
        content = self.request()
        data_to_csv = self.parsing(content)
        with open(f'Spam report\\agruped_by_ip.csv', 'w', newline='') as f:    
            writer = csv.writer(f)
            for line in data_to_csv:
                writer.writerow(line)


spam = agruped_by_ip()
spam.main()