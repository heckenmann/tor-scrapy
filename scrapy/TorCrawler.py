from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
import scrapy
import os
import requests
import json
import hashlib
import datetime
from urllib.parse import urlparse

class TorCrawler(CrawlSpider):
    name = "torcrawler"
    depth_limit=0
    start_urls = os.environ["urls"].split(",")
    allowed_domains = ["onion"]
    elasticsearch = os.environ["elasticsearch"]
    postSite = elasticsearch + "/crawler/page/"

    rules = (
        Rule(
            LxmlLinkExtractor(
                allow=(),
            ),
            follow=True,
            callback="parse_item",
        ),
    )

    def parse_item(self, response):
        current_page = {}
        current_page["title"] = response.css("head title ::text").extract_first()
        current_page["url"] = response.url
        current_page["timestamp"] = datetime.datetime.now().isoformat()
        print(current_page["url"])
        current_page["url_hash"] = hashlib.sha256(current_page["url"].encode('utf-8')).hexdigest()
        current_page["body"] = response.body.decode('utf-8')
        current_page["links"] = response.xpath("//a/@href").extract()
        current_page["http_status"] = response.status
        # Save to elasticsearch
        requests.post(self.postSite + current_page["url_hash"], data=json.dumps(current_page))

        return current_page
