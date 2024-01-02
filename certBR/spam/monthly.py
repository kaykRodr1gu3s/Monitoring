import requests
import bs4
import os
import csv


"""
the site that has been collected : https://stats.cert.br/spam/
"""

class monthly:
    def __init__(self) -> None:
        self.url = 'https://stats.cert.br/data/spam/2023/total-monthly.txt?_=1695660242177'
        os.chdir(os.getcwd() + '\\certBR\\spam')

    def mkdir(self): 
        try:
            os.mkdir('Spam report')
        except FileExistsError:
            print('Folder already exist')

    def request(self):
        req = requests.get(self.url)
        bs = bs4.BeautifulSoup(req.content, 'html.parser')
        return bs

    def parsing(self, bs4_content: bs4.BeautifulSoup):
        bs = bs4_content

        bs = bs.text.replace('#', '')
        bs = bs.replace('mes', 'month')
        bs = bs.replace('SW', 'Spamvertised')
        bs = bs.replace('(%)', 'percentage')
        bs = bs.replace('SS', 'sending_spam')
        bs = bs.replace('SP', 'proxy')
        bs = bs.replace('(%)', 'percentage')
        bs = bs.replace('SO', 'Outhers')
        bs = bs.replace('(%)', 'percentage')
        bs = bs.replace('unknown', 'other_sources')
        bs = bs.split('\n')

        data = []
        data_clear = []

        for value in bs:
            data.append(value.split())
        del data[0]
        del data[-1]

        for value in data:
            del value[6]
            del value[6]
            data_clear.append(value)
        return data_clear

    def main(self):
        self.mkdir()
        data_to_csv = self.parsing(self.request())
        with open(f'Spam report\\monthly.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            for data in data_to_csv:
                writer.writerow(data)


month = monthly()
month.main()
