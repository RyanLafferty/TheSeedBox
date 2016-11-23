from grocer.spiders.groceryspider import GrocerySpider

class MetroSpider(GrocerySpider):
    name = 'Metro'

    baseUrl = 'http://eflyer.metro.ca/MTR/MTRO/en/'
    categoryBlacklist = {'Home & Leisure'}
    extractProperties = ['ProductTitle', 'Price', 'CategoryName']

    def __init__(self):
        super(MetroSpider, self).__init__('NoFrills', MetroSpider.baseUrl, MetroSpider.categoryBlacklist, MetroSpider.extractProperties)