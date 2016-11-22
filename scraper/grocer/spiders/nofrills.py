import scrapy, json

class NoFrillsSpider(scrapy.Spider):
    name = 'No Frills'

    baseUrl = 'https://local.flyerservices.com/LCL/NOFR/en/'

    def start_requests(self):
        yield scrapy.Request(url=(NoFrillsSpider.baseUrl + 'Landing/GetClosestStoresByProvinceCity?countryCode=CA&province=ON&city=Guelph'), callback=self.get_cache_key)

    def get_cache_key(self, response):
        stores = json.loads(response.body_as_unicode())
        storeId = stores['Stores'][0]['StoreId']

        request = scrapy.Request(url=(NoFrillsSpider.baseUrl + 'Landing/CacheKey'), callback=self.get_publication_id)
        request.meta['store_id'] = storeId

        return request

    def get_publication_id(self, response):
        cache = json.loads(response.body_as_unicode())
        key = cache['Key']

        request = scrapy.Request(url=(NoFrillsSpider.baseUrl + 'Landing/GetPublicationsByStoreId?storeId=%s&key=%s' % (response.meta['store_id'], key)), callback=self.get_products)
        request.meta['store_id'] = response.meta['store_id']

        return request

    def get_products(self, response):
        publications = json.loads(response.body_as_unicode())

        for publication in publications['Publications']:
            request = scrapy.Request(url=(NoFrillsSpider.baseUrl + '%s/Product/ListAllProducts?storeId=%s' % (publication['PubId'], response.meta['store_id'])), callback=self.collect_products)
            request.meta['pub_id'] = publication['PubId']
            yield request

    def collect_products(self, response):
        print response.body_as_unicode()