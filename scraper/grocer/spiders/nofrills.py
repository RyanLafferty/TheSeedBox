from grocer.spiders.groceryspider import GrocerySpider

class NoFrillsSpider(GrocerySpider):
    name = 'NoFrills'

    baseUrl = 'https://local.flyerservices.com/LCL/NOFR/en/'
    categoryBlacklist = {'Home & Leisure'}
    extractProperties = ['ProductTitle', 'Price', 'CategoryName']

    def __init__(self):
        super(NoFrillsSpider, self).__init__('NoFrills', NoFrillsSpider.baseUrl, NoFrillsSpider.categoryBlacklist, NoFrillsSpider.extractProperties)