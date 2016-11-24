from grocer.spiders.groceryspider import GrocerySpider

class NoFrillsSpider(GrocerySpider):
    name = 'NoFrills'

    baseUrl = 'https://local.flyerservices.com/LCL/NOFR/en/'
    categoryWhitelist = {'Produce'}
    extractProperties = {'ProductTitle':'name', 'Price':'price'}

    def __init__(self):
        super(NoFrillsSpider, self).__init__('NoFrills', NoFrillsSpider.baseUrl, NoFrillsSpider.categoryWhitelist, NoFrillsSpider.extractProperties)