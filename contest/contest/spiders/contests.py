import scrapy
from contest.items import BrassbandItem
from scrapy.selector import Selector


class ContestsSpider(scrapy.Spider):
    name = 'contests'
    allowed_domains = ['www.musicabella.jp']
    start_urls = [
        "https://www.musicabella.jp/results/view?category=60&prefecture=14&region=4&year=2019&class=20&subclass=10"]

    def parse(self, response):
        sel = Selector(response)
        row = 5

        sample = sel.css(
            "div.container-fluid div div.col-md-10 table tbody tr td button:nth-child(1) a::text").extract()
        # ボタン
        sample2 = sel.xpath(
            "/html/body/div[3]/div/div[1]/table/tbody/tr["+str(row)+"]/td/button[1]/a").extract()

        # 全国
        sample3 = sel.css(
            "div.container-fluid div div.col-md-10 div.btn-group.btn-group-sm button:nth-child(1) a").extract()

        # 支部
        sample4 = sel.css(
            "div.container-fluid div div.col-md-10 div.btn-group.btn-group-sm div:nth-child(5) ul li a::text").extract()
        print("sample", sample2)

        for res in response.css("tr"):
            sel = Selector(response)
            title = sel.css("h1#page-heading::text").extract_first().split()
            year = title[0][:-1]
            if len(title) == 4:
                area = title[2][:-2]
                group = title[3][:-2]
            else:
                area = title[1][:-2]
                group = title[2][:-2]

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
