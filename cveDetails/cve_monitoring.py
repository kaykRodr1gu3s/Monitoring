import requests
import pandas as pd
import re
import bs4
import os

class cvedetails:
    def __init__(self) -> None:
        self.header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0'}
        self.link_base = 'https://www.cvedetails.com/cve/'
        self.all_data = {}
        self.cve_name = []
        self.base_score = []
        self.Base_Severity = []
        self.CVSS_Vector = []
        self.Exploitability_Score = []
        self.Exploitability_Score = []
        self.Impact_Score = []
        self.Source = []
        self.vendor = []
        self.link = []
      
    def directory(self):
        os.chdir(os.getcwd() + '\\cveDetails\\Csv datas')
      
    def get_page_content(self):
        url = requests.get(f'https://www.cvedetails.com/cisa-known-exploited-vulnerabilities/kev-1.html?&order=1&trc=988&sha=7cc3a9bfde72b01401aa6778d4ddc1b96eb2776d',
                        headers=self.header)
        
        bs = bs4.BeautifulSoup(url.content, 'html.parser')
        return bs

    def num_page_tot(self, page_content: bs4.BeautifulSoup):
        numbers_page = []
        num_pag = page_content.find_all('a', href=re.compile(r'/cisa-known-exploited-vulnerabilities/kev-\d+.html\?&order=1&trc=988&sha=7cc3a9bfde72b01401aa6778d4ddc1b96eb2776d'))
        del num_pag[0]

        for page in num_pag:

            numbers_page.append(page.text)

        return numbers_page
    def requests_for_cve_name(self,page_number: list):
        """
        this function will return a bs4.BeautifulSoup object, this function will accept a list with number of page    
        """
        cve_name = []

        for number in page_number:   
            req_base = requests.get(f'https://www.cvedetails.com/cisa-known-exploited-vulnerabilities/kev-{number}.html?&order=1&trc=988&sha=7cc3a9bfde72b01401aa6778d4ddc1b96eb2776d',
            headers=self.header)
            each_page = bs4.BeautifulSoup(req_base.content, 'html.parser')
            cve_names = each_page.find_all('a', href=re.compile(r'/cve/CVE-[\d]+-[\d]+'))

            for cve in cve_names:
                cve_name.append(cve.text)

        return cve_name

    def cve_content(self, names: list):
        for name in names:

            link = requests.get(self.link_base + name, headers=self.header)
            bs = bs4.BeautifulSoup(link.content,'html.parser')
            try:
                tables = bs.find('table', {'class': 'table table-borderless'})
                table_head = tables.thead.text.replace('\n', '#').split('#')
                del table_head[0]
                del table_head[-1]
                table_content = tables.tbody.tr.text.replace('\n', '# ').replace('\t', '').replace('#', '').strip().split()
                self.base_score.append(table_content[0])
                self.Base_Severity.append(table_content[1])
                self.CVSS_Vector.append(table_content[2])
                self.Exploitability_Score.append(table_content[3])
                self.Impact_Score.append(table_content[4])
                self.Source.append(table_content[5])

            except Exception as error:

                self.base_score.append('None')
                self.Base_Severity.append('None')
                self.CVSS_Vector.append('None')
                self.Exploitability_Score.append('None')
                self.Impact_Score.append('None')
                self.Source.append('None')

            
            try:
                vendors = bs.find('a', {'href': re.compile(r'/vendor/\d+/[A-Za-z\d/]+.html')}).text
                self.vendor.append(vendors)
            except Exception as error:

                self.vendor.append('None')


            self.link.append(self.link_base + name)
            self.cve_name.append(name)

            self.all_data['Name'] = self.cve_name 	    
            self.all_data['Base Score'] = self.base_score
            self.all_data['Base Severity'] = self.Base_Severity
            self.all_data['CVSS Vector'] = self.CVSS_Vector
            self.all_data['Exploitability Score'] = self.Exploitability_Score
            self.all_data['Impact Score'] = self.Impact_Score
            self.all_data['Source'] = self.Source
            self.all_data['Vendor'] = self.vendor
            self.all_data['Link'] = self.link


        return self.all_data

    def main(self):
        self.directory()
        get_page_content = self.get_page_content()
        num_page_tot = self.num_page_tot(get_page_content)
        requests_for_cve_name = self.requests_for_cve_name(num_page_tot)
        datas = self.cve_content(requests_for_cve_name)

        return datas

data_class = cvedetails()
df = pd.DataFrame(data_class.main())
df.to_csv('cvedetails.csv', index=False)
print('CSV created')


