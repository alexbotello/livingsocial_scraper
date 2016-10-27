from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Join, MapCompose

from scraper_app.items import LivingSocialDeal


class LivingSocialSpider(Spider):
    """Spider for regularly updated livingsocial.com site, Austin Page"""
    name = "livingsocial"
    allowed_domains = ['livingsocial.com']
    start_urls = ["https://www.livingsocial.com/cities/18-austin"]

    deals_list_xpath = '//li[@dealid]'
    item_fields = {
        'title': './/a/div[@class="deal-details"]/h3/text()',
        'link': './/a/@href',
        'location': './/a/div[@class="deal-details"]/p[@class="location"]/text()',
        'original_price': './/a/div[@class="deal-prices"]/div[@class="deal-strikethrough-price"]/div[@class="strikethrough-wrapper"]/text()',
        'price': './/a/div[@class="deal-prices"]/div[@class="deal-price"]/text()',
        'end_date': './/span[@itemscope]/meta[@itemprop="availabilityEnds"]/@content'
    }
    '//table[@class="data-table"]'

    def parse(self, response):
        """
        Default callback used by Scrapy to process downloaded responses
        """
        sel = Selector(response)

        # iterate over deals
        for deal in sel.xpath(self.deals_list_xpath):

            loader = ItemLoader(LivingSocialDeal(), selector=deal)

            # define processors
            loader.default_input_processor= MapCompose()
            loader.default_output_processor = Join()

            # iterate over fields and add xpaths to the Loader
            for field, xpath in self.item_fields.items():
                loader.add_xpath(field, xpath)
            yield loader.load_item()


#'.//span[@itemscope]/meta[@itemprop="name"]/@content'
