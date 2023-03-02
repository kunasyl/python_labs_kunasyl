import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime
import time
import re
from urllib.request import urlopen

from repos import Repos


class Services:

    repos = Repos()

    headers = {
        'accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }


    def get_resources(self):

        resources = self.repos.select_all_from_table("resources")
        resources_list = []
        
        for res in resources:
            resources_list.append(
                {
                    "url": res[1],
                    "base_url": res[2],
                    "url_template": res[3],
                    "article_div_class": res[4],
                    "article_title": res[5],
                    "article_url": res[6],
                    "time": res[7],
                    "article_date": res[8],
                    "article_content": res[9]
                }
            )

        return resources_list
    

    def check_url_connection(self, url):

        session = requests.Session()
        request = session.get(url, headers=self.headers)
        if request.status_code == 200:
            return True
        else:
            return False
    

    def get_urls_from_base_url(self, resource_url: dict, max_page_number=50):
        '''Get urls from base_url:
        - resource_url - resource url dict containing base_url, url_template
        - max_page_number - max pagination
        '''

        urls = []

        if self.check_url_connection(resource_url['base_url']):
            try:
                for page_number in range(max_page_number):
                    url = resource_url['url_template'].format(page_number=page_number)
                    if url not in urls:
                        urls.append(url)
            except:
                return f"Error"
        else:
            return f"Connection error"

        return urls

    
    def get_article_date(self, url: str) -> datetime:
        
        url_info = urlopen(url).info()
        # print('date: ', url_info['Date'])
        article_datetime = url_info['Date']
        if article_datetime:
            article_datetime = datetime.strptime(article_datetime, '%a, %d %b %Y %X %Z')
            # print(article_datetime)

        return article_datetime


    def parser(self, resource: dict):

        flats = []
        resource_id = self.get_resource_id(resource['url'])[0][0]
        urls = self.get_urls_from_base_url(resource_url=resource, max_page_number=1)
        session = requests.Session()

        for url in urls:
            request = session.get(url, headers=self.headers)
            soup = bs(request.content, 'lxml')
            divs = soup.find_all('div', attrs={'class': resource['article_div_class']})
            
            div_id = 1
            for div in divs:
                '''ID'''
                article_id = int(f"{resource_id}{div_id:05}")

                '''LINK'''
                article_url = div.find('a', attrs={'class': resource['article_url']})['href']
                article_abs_url = f"{resource['url']}{article_url}"
                # print("article_abs_url: ", article_abs_url)

                '''TITLE'''
                title = div.find('a', attrs={'class': resource['article_title']}).text.strip()
                # zakon.kz
                if not title:
                    title = div.find('div', attrs={'class': resource['article_title']})
                title = title.text.strip()
                # print("title: ", title)

                # time = div.find('div', attrs={'class': resource['time']}).text.strip()
                # print("time: ", time)

                '''CONTENT'''
                # get content from current news_url
                request = session.get(article_abs_url, headers=self.headers)
                soup = bs(request.content, 'lxml')
                content = soup.find('article', attrs={'class': resource['article_content']}).find_all('p')   
                content_text = ""
                for content_p in content:
                    content_text += content_p.text
                # print(content_text)

                '''DATE'''
                article_datetime = self.get_article_date(article_abs_url)
                if not article_datetime:
                    article_datetime = soup.find('div', attrs={'class': resource['article_date']}).text
                # print('article_datetime: ', article_datetime)

                flats.append((
                    article_id,                                       # id
                    resource_id,                                      # res_id
                    article_abs_url,                                  # link
                    title,                                            # title
                    content_text,                                     # content
                    self.convert_date_to_unix(article_datetime),      # nd_date
                    self.convert_date_to_unix(datetime.now()),        # s_date
                    datetime.strftime(article_datetime, '%Y-%m-%d')   # not_date
                ))

                div_id += 1

            # print(url)
            # print(len(flats))
            # sleep(randint(5,10))

        return flats


    def get_resource_id(self, resource_name: str):
        return self.repos.get_resource_id(resource_name)


    def insert_data_to_table(self, data: list):
        self.repos.insert_data_to_table(data)
        

    @staticmethod
    def convert_date_to_unix(datetime: datetime) -> str:
        return int(time.mktime(datetime.timetuple()))