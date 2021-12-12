import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from contest.items import BrassbandItem

"""
地区大会は地区によって構成がバラバラすぎるので、年と大会規模全部舐めないといけない(年と大会狙ってできない)
"""

ken_urls = [
    "http://www.musicabella.jp/results?category=50&prefecture=48",
    "http://www.musicabella.jp/results?category=50&prefecture=49",
    "http://www.musicabella.jp/results?category=50&prefecture=50",
    "http://www.musicabella.jp/results?category=50&prefecture=51",
    "http://www.musicabella.jp/results?category=50&prefecture=52",
    "http://www.musicabella.jp/results?category=50&prefecture=56",
    "http://www.musicabella.jp/results?category=50&prefecture=55",
    "http://www.musicabella.jp/results?category=50&prefecture=54",
    "http://www.musicabella.jp/results?category=50&prefecture=53",
    "http://www.musicabella.jp/results?category=50&prefecture=57",
    "http://www.musicabella.jp/results?category=50&prefecture=58",
    "http://www.musicabella.jp/results?category=50&prefecture=2",
    "http://www.musicabella.jp/results?category=50&prefecture=3",
    "http://www.musicabella.jp/results?category=50&prefecture=4",
    "http://www.musicabella.jp/results?category=50&prefecture=5",
    "http://www.musicabella.jp/results?category=50&prefecture=6",
    "http://www.musicabella.jp/results?category=50&prefecture=7",
    "http://www.musicabella.jp/results?category=50&prefecture=9",
    "http://www.musicabella.jp/results?category=50&prefecture=8",
    "http://www.musicabella.jp/results?category=50&prefecture=12",
    "http://www.musicabella.jp/results?category=50&prefecture=14",
    "http://www.musicabella.jp/results?category=50&prefecture=15",
    "http://www.musicabella.jp/results?category=50&prefecture=10",
    "http://www.musicabella.jp/results?category=50&prefecture=19",
    "http://www.musicabella.jp/results?category=50&prefecture=11",
    "http://www.musicabella.jp/results?category=50&prefecture=13",
    "http://www.musicabella.jp/results?category=50&prefecture=23",
    "http://www.musicabella.jp/results?category=50&prefecture=24",
    "http://www.musicabella.jp/results?category=50&prefecture=21",
    "http://www.musicabella.jp/results?category=50&prefecture=20",
    "http://www.musicabella.jp/results?category=50&prefecture=22",
    "http://www.musicabella.jp/results?category=50&prefecture=18",
    "http://www.musicabella.jp/results?category=50&prefecture=17",
    "http://www.musicabella.jp/results?category=50&prefecture=16",
    "http://www.musicabella.jp/results?category=50&prefecture=27",
    "http://www.musicabella.jp/results?category=50&prefecture=26",
    "http://www.musicabella.jp/results?category=50&prefecture=28",
    "http://www.musicabella.jp/results?category=50&prefecture=25",
    "http://www.musicabella.jp/results?category=50&prefecture=29",
    "http://www.musicabella.jp/results?category=50&prefecture=30",
    "http://www.musicabella.jp/results?category=50&prefecture=34",
    "http://www.musicabella.jp/results?category=50&prefecture=33",
    "http://www.musicabella.jp/results?category=50&prefecture=35",
    "http://www.musicabella.jp/results?category=50&prefecture=31",
    "http://www.musicabella.jp/results?category=50&prefecture=32",
    "http://www.musicabella.jp/results?category=50&prefecture=37",
    "http://www.musicabella.jp/results?category=50&prefecture=39",
    "http://www.musicabella.jp/results?category=50&prefecture=38",
    "http://www.musicabella.jp/results?category=50&prefecture=36",
    "http://www.musicabella.jp/results?category=50&prefecture=40",
    "http://www.musicabella.jp/results?category=50&prefecture=41",
    "http://www.musicabella.jp/results?category=50&prefecture=42",
    "http://www.musicabella.jp/results?category=50&prefecture=43",
    "http://www.musicabella.jp/results?category=50&prefecture=46",
    "http://www.musicabella.jp/results?category=50&prefecture=45",
    "http://www.musicabella.jp/results?category=50&prefecture=44",
    "http://www.musicabella.jp/results?category=50&prefecture=47"
]


class ContestCrawlSpider(CrawlSpider):
    name = 'contest_crawl'
    allowed_domains = ['www.musicabella.jp']
    start_urls = ken_urls
    row = 5

    rules = (
        Rule(
            LinkExtractor(
                restrict_xpaths="/html/body/div[3]/div/div[1]/table/tbody/tr/td/button[1]/a"),
            callback='parse'
        ),
        # 地区
        Rule(
            LinkExtractor(
                restrict_css="div.container-fluid div div.col-md-10 div.btn-group.btn-group-sm div:nth-child(5) ul li a"),
        ),
    )
    """
    # 全国大会
        Rule(
            LinkExtractor(
                restrict_css="div.container-fluid div div.col-md-10 div.btn-group.btn-group-sm button:nth-child(1) a"),
        ),
        # 支部
        Rule(
            LinkExtractor(
                restrict_css="div.container-fluid div div.col-md-10 div.btn-group.btn-group-sm div:nth-child(3) ul li a"),
        ),
        # 県
        Rule(
            LinkExtractor(
                restrict_css="div.container-fluid div div.col-md-10 div.btn-group.btn-group-sm div:nth-child(4) ul li a"),
        ),
    """

  # 支部大会

    def parse_shibu(self, response):
        sel = Selector(response)
        title = sel.css("h1#page-heading::text").extract_first().split()
        year = title[0][:-1]
        area = title[2][:-2]
        group = title[3][:-2]

        sample = sel.css(
            "div.container-fluid div div.col-md-10 div.btn-group.btn-group-sm button.btn.btn-default a::text").extract()
        print("sample", sample)

        for res in response.css("tr"):
            item = BrassbandItem()
            item['region'] = res.css('td a span.region::text').extract_first()
            item['school'] = res.css(
                'td a:nth-child(2)::text').extract_first()
            item["conductor"] = res.css(
                'td a:nth-child(3)::text').extract_first()
            item["taskSongNum"] = res.css(
                "td span.kadai::text").extract_first()
            item["taskSongName"] = res.css(
                'td a:nth-child(7)::text').extract_first()
            item["freeSongName"] = res.css(
                'td a:nth-child(10)::text').extract_first()
            item["freeSongWriter"] = res.css(
                'td a:nth-child(11)::text').extract_first()
            item["prize"] = res.css("td span.prize::text").extract_first()
            item["consertArea"] = area
            item["year"] = year
            item["group"] = group

            yield item

    def parse_start_url(self, response):
        return

    # 全国大会

    def parse_zenkoku(self, response):
        sel = Selector(response)
        title = sel.css("h1#page-heading::text").extract_first().split()
        year = title[0][:-1]
        area = title[2][:-2]
        group = title[3][:-2]

        for res in response.css("tr"):
            item = BrassbandItem()
            item['region'] = res.css('td a span.region::text').extract_first()
            item['school'] = res.css(
                'td a:nth-child(3)::text').extract_first()
            item["conductor"] = res.css(
                'td a:nth-child(4)::text').extract_first()
            item["taskSongNum"] = res.css(
                "td span.kadai::text").extract_first()
            item["taskSongName"] = res.css(
                'td a:nth-child(8)::text').extract_first()
            item["freeSongName"] = res.css(
                'td a:nth-child(11)::text').extract_first()
            item["freeSongWriter"] = res.css(
                'td a:nth-child(12)::text').extract_first()
            item["prize"] = res.css("td span.prize::text").extract_first()
            item["consertArea"] = area
            item["year"] = year
            item["group"] = group

            yield item

    #　県大会
    def parse_ken(self, response):
        sel = Selector(response)
        title = sel.css("h1#page-heading::text").extract_first().split()
        year = title[0][:-1]
        area = title[2][:-2]
        group = title[3][:-2]
        print("title", title)

        for res in response.css("tr"):
            item = BrassbandItem()
            item['region'] = res.css('td a span.region::text').extract_first()
            item['school'] = res.css(
                'td a:nth-child(1)::text').extract_first()
            item["conductor"] = res.css(
                'td a:nth-child(2)::text').extract_first()
            item["taskSongNum"] = res.css(
                "td span.kadai::text").extract_first()
            item["taskSongName"] = res.css(
                'td a:nth-child(6)::text').extract_first()
            item["freeSongName"] = res.css(
                'td a:nth-child(9)::text').extract_first()
            item["freeSongWriter"] = res.css(
                'td a:nth-child(10)::text').extract_first()
            item["prize"] = res.css("td span.prize::text").extract_first()
            item["consertArea"] = area
            item["year"] = year
            item["group"] = group

            yield item

    # 地区大会
    def parse_chiku(self, response):
        sel = Selector(response)
        title = sel.css("h1#page-heading::text").extract_first().split()
        year = title[0][:-1]
        if len(title) == 4:
            area = title[2][:-2]
            group = title[3][:-2]
        else:
            area = title[1][:-2]
            group = title[2][:-2]

        for res in response.css("tr"):
            representative = res.css(
                'td:nth-child(3)::text').extract()

            item = BrassbandItem()

            if len(representative) != 0 and representative[-1][:3] == "・代表":
                item["representative"] = True
            else:
                item["representative"] = False

            item['region'] = res.css('td a span.region::text').extract_first()
            item['school'] = res.css(
                'td a:nth-child(1)::text').extract_first()
            item["conductor"] = res.css(
                'td a:nth-child(2)::text').extract_first()
            item["taskSongNum"] = res.css(
                "td span.kadai::text").extract_first()
            item["taskSongName"] = res.css(
                'td a:nth-child(6)::text').extract_first()
            item["freeSongName"] = res.css(
                'td a:nth-child(9)::text').extract_first()
            item["freeSongWriter"] = res.css(
                'td a:nth-child(10)::text').extract_first()
            item["prize"] = res.css("td span.prize::text").extract_first()
            item["consertArea"] = area
            item["year"] = year
            item["group"] = group

            yield item

    def parse(self, response):
        sel = Selector(response)
        title = sel.css("h1#page-heading::text").extract_first().split()
        year = title[0][:-1]

        if len(title) == 4:
            size = title[2][-4:]
            group = title[3][:-2]
        else:
            size = title[1][-4:]
            group = title[2][:-2]

        if int(year) >= 2013 and int(year) <= 2017:
            if group == "高校A" and size == "地区大会":
                return self.parse_chiku(response)
