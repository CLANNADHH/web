import requests
import random
import json
import re
# from retry import retry
from hhblog.settings import MEDIA_ROOT


class CatchNews(object):
    def __init__(self,path=None):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3\
            497.100 Safari/537.36',
            'Host': 'news.163.com',
        }
        self.url = "http://news.163.com/special/0001220O/news_json.js?"
        if path:
            self.file_path = MEDIA_ROOT + '/news.txt'
        else:
            self.file_path = './news.txt'

    # @retry(tries=3)
    def send_request(self):
        response = requests.get(self.url+str(random.random()),headers=self.headers)
        # response = requests.get(self.url+'0.9732076378302217',headers=self.headers)
        print(response.headers.get('Content-Type'))
        rule = re.compile(r'({.*?})')
        result = rule.findall(response.content.decode('gbk'))

        result_list = []
        # print(result)
        for line in result:
            result_list.append(json.loads(line))
        news_dict = json.dumps(result_list)
        news_dict = json.loads(news_dict)
        count = 0
        file_count = 0

        with open(self.file_path, 'w') as f:
            for i in news_dict:
                if i.get('c') is not None:
                    news_dict[count]['c'] = news_dict[i['c']]['n']
                    file_count += 1
                    if count > 8 and news_dict[count]['c'] != news_dict[count-1]['c']:
                        file_count = 0
                if 1<= file_count <= 10:
                    f.write(str(news_dict[count])+',\n')
                count += 1
        return news_dict

    def parse_news(self):
        news_list = []
        try:
            with open(self.file_path, 'r') as f:
                while True:
                    news = f.readline()
                    if news != '':
                        temp = eval(news[0:-2])
                        # temp = json.loads(temp)
                        # print(type(temp))
                        news_list.append(temp)
                    else:
                        break
        except:
            return []
        return news_list

if __name__ == "__main__":
    c = CatchNews(1)
    c.send_request()
    # print(c.parse_news()
    c.parse_news()