import scrapy, json
from grocer.items import Product

class GrocerySpider(scrapy.Spider):
    def __init__(self, name, baseUrl, categoryBlacklist, extractProperties):
        super(GrocerySpider, self).__init__(name=name)
        self.baseUrl = baseUrl
        self.categoryBlacklist = categoryBlacklist
        self.extractProperties = extractProperties

    def start_requests(self):
        yield scrapy.Request(url=(self.baseUrl + 'Landing/GetClosestStoresByProvinceCity?countryCode=CA&province=ON&city=Guelph'), callback=self.get_cache_key)

    def get_cache_key(self, response):
        stores = json.loads(response.body_as_unicode())
        storeId = stores['Stores'][0]['StoreId']

        request = scrapy.Request(url=(self.baseUrl + 'Landing/CacheKey'), callback=self.get_publication_id)
        request.meta['store_id'] = storeId

        return request

    def get_publication_id(self, response):
        cache = json.loads(response.body_as_unicode())
        key = cache['Key']

        request = scrapy.Request(url=(self.baseUrl + 'Landing/GetPublicationsByStoreId?storeId=%s&key=%s' % (response.meta['store_id'], key)), callback=self.get_products)
        request.meta['store_id'] = response.meta['store_id']

        return request

    def get_products(self, response):
        publications = json.loads(response.body_as_unicode())

        for publication in publications['Publications']:
            request = scrapy.Request(url=(self.baseUrl + '%s/Product/ListAllProducts?storeId=%s' % (publication['PubId'], response.meta['store_id'])), callback=self.collect_products)
            request.meta['pub_id'] = publication['PubId']
            yield request

    def collect_products(self, response):
        products = json.loads(response.body_as_unicode())

        for productObject in products['Products']:
            if productObject['CategoryName'] not in self.categoryBlacklist:
                product = Product(name=productObject['ProductTitle'], price=productObject['Price'], priceUnit=productObject['PriceUnit'])
                yield product