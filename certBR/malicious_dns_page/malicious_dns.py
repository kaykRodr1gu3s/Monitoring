import requests
import bs4
import csv
import os


"""the page that i am collecting is : https://stats.cert.br/dns-malicioso/"""

class DNS:
    def __init__(self):
        self.url = 'https://stats.cert.br/data/dns-malicioso/dns-br-notbr.txt'
        os.chdir(os.getcwd() + '\\certBR\\malicious_dns_page')
    
    
    def makedir(self):    
      
        folder_name = 'Malicious'
        try:
            os.mkdir(folder_name)
            print('Folder created')
        except FileExistsError:
            print('folder already exist')
        

    def request(self):
        req = requests.get(self.url)

        bs = bs4.BeautifulSoup(req.content,'html.parser')
        return bs
    
    def parsing(self, request_content: bs4.BeautifulSoup):
        bs4 = request_content.text.split('\n')

        del bs4[0]
        clear = []

        for c in bs4:
            bs4 = c.replace('#', '')
            bs4 = bs4.strip()
            bs4 = bs4.split()
            clear.append(bs4)

        return clear
    
    def main(self):
        self.makedir()
        request_content = self.request()
        data_to_csv = self.parsing(request_content)   
        
        with open(f'Malicious\\Malicious.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data_to_csv)
 



Malicious = DNS()
Malicious.main()

