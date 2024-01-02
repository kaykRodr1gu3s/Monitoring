import requests
import bs4
import csv
import os


"""
the site that has been collected : https://stats.cert.br/spam/
"""

class spam:
    def __init__(self):
        self.url = 'https://stats.cert.br/data/spam/spam-stats-ym.txt'
        os.chdir(os.getcwd() + '\\certBR\\spam')

    def mkdir(self):
        try:
            os.mkdir('Spam report')
            print('folder created')
        except FileExistsError:
            print('Folder already exist')

    def request(self):
        req = requests.get(self.url)
        bs = bs4.BeautifulSoup(req.content, 'html.parser')
        return bs
    
    def parsing(self, bs4_content: bs4.BeautifulSoup):
        bs = bs4_content
        data_clear = []

        bs = bs.text.replace('#', '')
        bs = bs.split('\n')

        del bs[0]
        del bs[0]
        del bs[0]
        del bs[-1]

        for value in bs:
            bs = value.split()
            data_clear.append(bs)

        return data_clear
    
    def main(self):
        self.mkdir()
        data_to_csv = self.parsing(self.request())
        
        with open(f'Spam report\\by_year.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            for data in data_to_csv:
                writer.writerow(data)

by_year = spam()
by_year.main()

