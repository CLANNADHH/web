from until.get_news import CatchNews


def generate_news_file():
    c = CatchNews(1)
    c.send_request()
