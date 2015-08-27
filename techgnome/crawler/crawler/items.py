import scrapy

class ReleaseItem(scrapy.Item):
    artist = scrapy.Field()
    release = scrapy.Field()
    genre = scrapy.Field()
    label = scrapy.Field()
    date = scrapy.Field()
    tags = scrapy.Field()
