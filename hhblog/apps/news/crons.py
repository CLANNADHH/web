from until.get_news import catch_news


def generate_news_file():
    c = catch_news(1)
    c.send_request()
