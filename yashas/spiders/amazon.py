import scrapy
from urllib.parse import urlencode

import json

# itobj = open('it.json', )
# itdata = json.load(itobj)

#frobj = open('fr.json', )
#frdata = json.load(frobj)
#deobj=open('de.json',)
#dedata=json.load(deobj)
esobj=open('es.json',)
esdata=json.load(esobj)


API = 'c39d2763f9aea5a2a8f9c6d4bcdd33b4'


def get_url(url):
    payload = {'api_key': API, 'url': url}
    proxy_url = 'http://api.scraperapi.com/?' + urlencode(payload)
    return proxy_url


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = ['http://amazon.com/']
    custom_settings = {
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
    }

    def start_requests(self):
        url = 'https://www.amazon.es/'
        yield scrapy.Request(url=get_url(url),
                             callback=self.parse_keyword_response)

    def parse_keyword_response(self, response):
        for asins in esdata['essheet']:
            asin = asins['Asin']
            product_url = f"https://www.amazon.es/dp/{asin}"
            if product_url:
                yield scrapy.Request(url=get_url(product_url),
                                     callback=self.parse_product_page, meta={'asin': asin})
            else:
                yield {'error': 404}

    def parse_product_page(self, response):
        title = response.xpath('//*[@id="productTitle"]/text()').extract_first()
        # image = response.xpath('/*[@id = "imgTagWrapperId] ').extract_first()

        # price = response.xpath(
        # '//*[(@id = "corePrice_feature_div")] | //*[(@id = "ddmDeliveryMessage")]//font').extract_first()

        # if not price:
        # price = response.xpath('//*[@data-asin-price]/@data-asin-price').extract_first()
        yield {'Title': title

               }
