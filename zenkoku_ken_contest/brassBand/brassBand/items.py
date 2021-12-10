# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BrassbandItem(scrapy.Item):
    school = scrapy.Field()
    conductor = scrapy.Field()
    prize = scrapy.Field()
    taskSongName = scrapy.Field()
    taskSongNum = scrapy.Field()
    freeSongName = scrapy.Field()
    freeSongWriter = scrapy.Field()
    year = scrapy.Field()
    region = scrapy.Field()
    consertArea = scrapy.Field()
    group = scrapy.Field()
    representative = scrapy.Field()


class ContestItem(scrapy.Item):
    url = scrapy.Field()
    headline = scrapy.Field()
    category = scrapy.Field()
