import requests
from bs4 import BeautifulSoup
import datetime

class Paste_fo:

    def __init__(self):
        self.request_base = 'https://paste.fo/recent'
        self.datas = {}
    

    def paste_id(self, pages) -> list:
        """
        
        it will return all the href link from all paste able, the total is 75
        
        """
        paste_href = []

        req = requests.get(f'{self.request_base}/{pages}')
        bs4 = BeautifulSoup(req.content, 'html.parser')
        posts = bs4.find_all('tr')


        for post in posts:
            if not post.get('class'):
                link = post.find('a')['href']
                paste_href.append(link)
                
        return paste_href

    def username(self, pastes_id) -> list:
        """
        take the paste_id function as argument
        it will return a list with usernames 
        
        """
        usernames = []
        for link in pastes_id:

            req = requests.get(f'https://paste.fo{link}')
            
            bs4 = BeautifulSoup(req.content, 'html.parser')
            names = bs4.find('h3', class_='paste-info larger') 

            usernames.append(names.text)

        return usernames
    

    def info_details(self, pages) -> list:
         """
         as input pass the paste_id
         this function will return a list of content details, there is some pastes that have nothting, will return a simple text with the paste link
          
         """
 
         datas = {}
         all_data = []

 
         for link in pages:
 
            details = []
            req = requests.get(f'https://paste.fo{link}')
            

            try:
                bs4 = BeautifulSoup(req.content, 'html.parser')
                bs4 = bs4.find_all('span', {'class': 'about-value'})

                for data in bs4:

                    details.append(data.text)
                     
                time = details[-1]
                time = time.split()
 
                if time[1] in "minutes":
                    time_created = datetime.datetime.now() - datetime.timedelta(minutes=int(time[0]))
                    fortatted_string = time_created.strftime("%Y-%m-%d %H:%M:%S")
                    details[-1] = fortatted_string
 
                elif time[1] in 'hours' or 'hour':
                    time_created = datetime.datetime.now() - datetime.timedelta(hours=int(time[0]))
                    fortatted_string = time_created.strftime("%Y-%m-%d %H:%M:%S")
                    details[-1] = fortatted_string
  
            except:
 
                details.append(f'the folder on https://paste.fo{link} doesnt exist')
 
            datas["statistics"] = f' Views : {details[0]}, Visibility :"{details[1]}, Expires : {details[2]}, Created : {details[3]}'
            all_data.append(datas)
         

         return all_data
    

    def raw_details(self, pages) -> list:
        """
        this function, will return the raw content from each paste

        """

        content = []
 
        for link in  pages:
 
            req = requests.get(f'https://paste.fo/raw{link}')
 
            bs4 = req.text
            bs4 = bs4.replace('\r\n', '')
            content.append(bs4)
        return content
 
    def about_users(self,username) -> list:
        """
        the function will return the content from user, as users contact and the statistics
       """
 
        statistics = []
        content = []
        raw_content = []
        

        for c in username:
            user_details = []
            req = requests.get(f'https://paste.fo/user/{c}')
            bs4 = BeautifulSoup(req.content, 'html.parser')
 
            view_details = bs4.find_all('span', {'class': 'about-value'})
            for c in view_details:

                user_details.append(c.text)
 
            try:
                contact = bs4.find_all('div', {'class':'profilecontact'})
                for c in contact:
                    user_details.append(c.a['href'])
 
            except:
                user_details.append('There no telegram contact')
 
            try:
                contact = bs4.find('h4', {'class': 'profileattribute'})
                user_details.append(contact.text.strip())
            except:
                user_details.append('there no discord contact')
            statistics.append(user_details)

        

        return statistics

main = Paste_fo()


for k,c in enumerate(range(1, 6)):
    data = []
    pages = main.paste_id(c)
    user = main.username(pages)
    info = main.info_details(pages)
    about = main.about_users(user)
    raw_content = main.raw_details(pages)
    data.append({'User': user[k], 'About':{'Folders': about[k][0], 'Views': about[k][1]},'Page info details': [info[k],f'https://paste.fo{pages[k]}'], "description": raw_content}) 
    print(data)

print('All datas was collected')
