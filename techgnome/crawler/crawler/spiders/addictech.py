import scrapy
from crawler.items import ReleaseItem

class ATechSpider(scrapy.Spider):
    name = 'ATech'
    allowed_domains = ['addictech.com']
    start_urls = [
        'http://www.addictech.com/?keywords=tipper&type=album'
    ]

    def parse(self, response):

        for sel in response.xpath("//table[@class='productListing']/tr/td[2]/div[1]/table/tr/td[1]"):
            item = ReleaseItem()
            item['artist'] = sel.xpath("table/tr[1]/td[2]/a/text()").extract()
            item['label'] = sel.xpath("table/tr[2]/td[2]/a/text()").extract()
            item['genre'] = sel.xpath("table/tr[3]/td[2]/text()").extract()
            item['release'] = sel.xpath("div[1]/text()").extract()
            item['date'] = sel.xpath("table/tr[5]/td[2]/text()").extract()

            tags = []
            tag_sel = sel.xpath("table/tr[4]/td[2]")
            for t in tag_sel:
                tags.append(t.xpath("a/text()").extract())
            item['tags'] = tags
            yield item