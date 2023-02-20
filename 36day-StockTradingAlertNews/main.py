from stock import Stock
from news import News
from alert import Alert
from datetime import datetime

STOCK = ["WDAY", "GWRE"]

for s in STOCK:
    stock = Stock(s)
    stock.parse_stock_trade()
    stock_oscillation = stock.get_percentage(float(stock.stock_close_yesterday), float(stock.stock_close_before_yesterday))
    if stock_oscillation > 5 or stock_oscillation < -5:
        news = News(STOCK)
        news.get_news()
        alert = Alert()
        alert.send_news_sms(msg = news.article_list, stock = s, percent = stock_oscillation)
    else:
        print(f"{datetime.now()} - {stock.stock}: {int(stock_oscillation)}% oscilation from the day before yesterday and yesterday")