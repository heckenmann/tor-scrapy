FROM python:3.6.1

RUN pip install scrapy
RUN pip install requests
RUN mkdir /crawler
WORKDIR /crawler
ADD TorCrawler.py .

CMD scrapy runspider TorCrawler.py
