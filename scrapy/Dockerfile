FROM python:3.9

RUN pip install --upgrade pip
RUN pip install scrapy
RUN pip install requests
RUN mkdir /crawler
WORKDIR /crawler
ADD TorCrawler.py .

CMD scrapy runspider TorCrawler.py
