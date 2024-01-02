import requests
import bs4
import csv
import os


'''
"""the page that i am collecting is : https://stats.cert.br/vulns/"""
'''
class Vulnerable_services:
    def __init__(self):
        self.url = 'https://stats.cert.br/data/vulns/summary_stats.txt?_=1695607191486'
        os.chdir(os.getcwd() + '\\certBR\\Vulnerable_services')


    def mkdir(self):
        try:
            os.mkdir('Vulnerable services')
            print('Folder created')
        except FileExistsError:
            print('Folder already exist')

    def request(self):
        req = requests.get(self.url)
        bs = bs4.BeautifulSoup(req.content, 'html.parser')
        return bs
    
    def parsing(self, bs4_content: bs4.BeautifulSoup):
        bs = bs4_content
        head = ['', 'Zimbra', 'Zimbra', 'VMware', 'VMware', 'MS-Exchange', 'MS-Exchange']
        clear_data = [head]

        for value in bs:
            cleaning = value.text.split('\n')

            for data in cleaning:
                cleaning = data.replace('zimbra_asns','ASN')
                cleaning = cleaning.replace('zimbra_ips', 'IP')
                cleaning = cleaning.replace('vmware_asns', 'ASN')
                cleaning = cleaning.replace('vmware_ips', 'IP')
                cleaning = cleaning.replace('exchange_asns', 'ASN')
                cleaning = cleaning.replace('exchange_ips', 'IP')
                cleaning = cleaning.split('|') 
                clear_data.append(cleaning)

        del clear_data[-1]

        return  clear_data

    def main(self):
        self.mkdir()
        content = self.parsing(self.request())
        
        with open(f'Vulnerable services\\Vulnerable_services.csv', 'w', newline='') as f:
            writter = csv.writer(f)
            for line in content:
                writter.writerow(line)

vulnerable = Vulnerable_services()
vulnerable.main()
