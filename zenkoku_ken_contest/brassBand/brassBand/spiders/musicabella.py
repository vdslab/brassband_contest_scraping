import scrapy
from brassBand.items import BrassbandItem
from scrapy.selector import Selector


class MusicabellaSpider(scrapy.Spider):
    name = 'musicabella'
    allowed_domains = ['www.musicabella.jp']
    # start_urls = ['http://www.musicabella.jp/']
    start_urls = [
        "https://www.musicabella.jp/results/view?category=50&prefecture=14&year=2017&class=20&subclass=10"]

    def parse(self, response):
        sel = Selector(response)
        title = sel.css("h1#page-heading::text").extract_first().split()
        year = title[0][:-1]
        area = title[2][:-2]
        group = title[3][:-2]
        print("title", title)

        sample = sel.css(
            "div.container-fluid div div.col-md-10 div.btn-group.btn-group-sm div:nth-child(4) ul li a::text").extract()
        print("sample", sample)

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
