import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from contest.items import SchoolName
from scrapy.selector import Selector
import re


class GetSchoolNameSpider(CrawlSpider):
    name = 'get_school_name'
    allowed_domains = ['www.musicabella.jp']
    start_urls = ['https://www.musicabella.jp/groups/']

    rules = (
        Rule(LinkExtractor(
            restrict_xpaths="/html/body/div[3]/div/div[1]/table/tbody/tr/td[3]/a"), callback='parse_item'),
    )

    def parse_item(self, response):
        sel = Selector(response)
        title = sel.xpath(
            "/html/body/div[3]/div/div[1]/h1/text()").extract_first()
        prefecture = re.split(' |（', title)[1]

        # prefecture =

        for res in response.css("tr"):
            item = SchoolName()
            item["name"] = res.css("th a::text").extract()
            item["prefecture"] = prefecture
            yield item
