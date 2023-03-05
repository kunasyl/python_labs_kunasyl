import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime
import time
from urllib.request import urlopen
from time import sleep
from random import randint

from repos import Repos


class Services:

    repos = Repos()

    headers = {
        'accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }


    def get_resources(self) -> list:
        '''Convert data from resources table into a dictionary for the usefullness'''

        resources = self.repos.select_all_from_table("resources")
        resources_list = []
        
        for res in resources:
            resources_list.append(
                {
                    "url": res[1],
                    "url_template": res[2],
                    "articles_class": res[3],
                    "article_title": res[4],
                    "article_url": res[5],
                    "article_content": res[6]
                }
            )

        return resources_list
    

    def check_url_connection(self, url: str) -> bool:
        '''Check the connection to by a given url'''

        session = requests.Session()
        request = session.get(url, headers=self.headers)
        if request.status_code == 200:
            return True
        else:
            return False
    

    def get_urls_from_base_url(self, url_template: str, max_page_number=10):
        '''Get urls from base url:
        - resource_url - resource url tuple containing base url, url_template
        - max_page_number - max pagination
        '''

        urls = []

        for page_number in range(1, max_page_number+1):
            url = url_template.format(page_number=page_number)
            if url not in urls:
                urls.append(url)

        return urls

    
    def get_article_date(self, url: str) -> datetime:
        '''Get datetime from the website (last edited date)'''
        
        url_info = urlopen(url).info()
        article_datetime = url_info['Date']
        if article_datetime:
            article_datetime = datetime.strptime(article_datetime, '%a, %d %b %Y %X %Z')

        return article_datetime
    

    def parse_data_and_insert(self, resource: dict, max_page_number=10):
        '''Parse all urls from news website and insert into the table items'''
        urls = self.get_urls_from_base_url(resource['url_template'], max_page_number)

        url_id = 1
        for url in urls:
            url_articles = self.parse_url_page(url, resource, url_id)
            print('Expected insert data count: ', len(url_articles))
            self.insert_data_to_items(url_articles)
            url_id += 1


    def parse_url_page(self, url: str, resource: dict, url_id: int):
        '''Parse news from a given url page:
        - resource - resource dictionary contains infromation about a website
        - max_page_number - max pagination (how much pages of the website we want to parse)
        '''

        flats = []
        resource_id = self.get_resource_id(resource['url'])[0][0]
        session = requests.Session()

        request = session.get(url, headers=self.headers)
        soup = bs(request.content, 'lxml')
        divs = soup.find_all(
            name=('div' or 'a'),
            attrs={'class': resource['articles_class']}
        )
        
        div_id = 1
        for div in divs:
            '''ID'''
            article_id = int(f"{resource_id}{url_id:02}{div_id:02}")

            '''LINK'''
            article_url = div.find(
                name='a', 
                attrs={'class': resource['article_url']}
            )['href']
            article_abs_url = f"{resource['url']}{article_url}"
            print(f"{article_abs_url} with id: {article_id}")

            '''TITLE'''
            title = div.find(
                name=('a' or 'div'), 
                attrs={'class': resource['article_title']}
            )
            if not title:
                title = div.find('div', attrs={'class': 'title'})
            title = title.text.strip()

            '''CONTENT'''
            if not self.check_url_connection(article_abs_url):
                continue
            request = session.get(article_abs_url, headers=self.headers)
            soup = bs(request.content, 'lxml')
            content = soup.find(
                name=('article', 'div'),
                attrs={'class': resource['article_content']}
            ).find_all('p')
            content_text = ""
            for content_p in content:
                content_text += content_p.text.strip()

            '''DATE'''
            article_datetime = self.get_article_date(article_abs_url)

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
            sleep(randint(5,10))

        return flats


    def get_resource_id(self, resource_name: str):
        return self.repos.get_resource_id(resource_name)


    def insert_data_to_items(self, data: list):
        self.repos.insert_data_to_items(data)
        

    @staticmethod
    def convert_date_to_unix(datetime: datetime) -> str:
        return int(time.mktime(datetime.timetuple()))