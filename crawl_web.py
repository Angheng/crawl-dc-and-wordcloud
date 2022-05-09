from bs4 import BeautifulSoup
import requests


def packaging(raw):
    article_list = []

    for i in raw:
        bs = BeautifulSoup(i, 'html.parser')

        for article in bs.find('tbody').find_all('tr'):
            sbj = article.find('td', class_='gall_subject').find('b')
            if sbj is None:
                article_list.append(
                    {
                        "title": article.find('a').text,
                        "nickname": article.find('td', class_='gall_writer ub-writer').find('span',
                                                                                            class_='nickname').text,
                        "date": article.find('td', class_='gall_date')['title'],
                        "gaechu": article.find('td', class_='gall_recommend').text
                    }
                )

    return article_list


class Crawl:

    def __init__(self):
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73 '
        }

        self.targ_url = ""

    def crawl_pageBase(self, page):
        print('=' * 50)
        parse = []

        for i in range(1, page + 1):

            req = requests.get(
                self.targ_url + '&page=' + str(i), headers=self.header
            )

            parse.append(req.text)
            print('crawled', i, 'page.')

        print('='*50)

        return packaging(parse)

    def set_url(self, url):
        self.targ_url = url
