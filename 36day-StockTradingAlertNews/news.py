import requests
import os

URL = "https://newsapi.org/v2/everything"

class News:
    
    def __init__(self, company):
        try:
            API_KEY = os.environ.get('NEWS_API_KEY')
        except:
            raise Exception("Environment variable NEWS_API_KEY doesn't exist")
        else:
            self.param = { "q": company,
                        "sortby": "relevancy",
                        "pageSize": 3,
                        "apiKey": API_KEY
                    }
        self.article_list = []
        
    def fetch_data(self):
        r = requests.get(URL, params=self.param)
        r.raise_for_status()
        self.data = r.json()
        
    def get_news(self):
        try:
            self.fetch_data()
        except:
            raise Exception("Fetch data news error")
        else:
            for i in self.data['articles']:
                self.media_name = i['source']['name']
                self.news_title = i['title']
                self.news_desc = i['description']
                self.news_date = i['publishedAt']
                self.news_url = i['url']
                t = (self.media_name, self.news_title, self.news_desc, self.news_date, self.news_url)
                self.article_list.append(t) 