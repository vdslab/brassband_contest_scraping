import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from brassBand.items import BrassbandItem
from scrapy.selector import Selector


class ContestcrawlSpider(CrawlSpider):
    name = 'contestCrawl'
    allowed_domains = ['www.musicabella.jp']
    start_urls = ['https://www.musicabella.jp/results/view?category=30&branch=10&year=2017&class=20&subclass=10', 'https://www.musicabella.jp/results/view?category=30&branch=10&year=2016&class=20&subclass=10', 'https://www.musicabella.jp/results/view?category=30&branch=10&year=2015&class=20&subclass=10',
                  'https://www.musicabella.jp/results/view?category=30&branch=10&year=2014&class=20&subclass=10', 'https://www.musicabella.jp/results/view?category=30&branch=10&year=2013&class=20&subclass=10']

    rules = (
        Rule(
            LinkExtractor(
                restrict_css="div.container-fluid div div.col-md-10 div.btn-group.btn-group-sm button a"),
            callback='parse_zenkoku'
        ),
        Rule(
            LinkExtractor(
                restrict_css="div.container-fluid div div.col-md-10 div.btn-group.btn-group-sm div:nth-child(4) ul li a"),
            callback='parse_ken'
        ),
        Rule(
            LinkExtractor(
                restrict_css="div.container-fluid div div.col-md-10 div.btn-group.btn-group-sm div:nth-child(3) ul li a"),
            callback='parse'
        ),
    )

    # 支部大会

    def parse(self, response):
        sel = Selector(response)
        title = sel.css("h1#page-heading::text").extract_first().split()
        year = title[0][:-1]
        area = title[2][:-2]
        group = title[3][:-2]

        sample = sel.css(
            "div.container-fluid div div.col-md-10 div.btn-group.btn-group-sm button.btn.btn-default a::text").extract()
        print("sample", sample)

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
        return self.parse(response)

    # 全国大会
    def parse_zenkoku(self, response):
        sel = Selector(response)
        title = sel.css("h1#page-heading::text").extract_first().split()
        year = title[0][:-1]
        area = title[2][:-2]
        group = title[3][:-2]

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
