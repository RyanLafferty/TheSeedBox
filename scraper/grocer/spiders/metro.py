from grocer.spiders.groceryspider import GrocerySpider

class MetroSpider(GrocerySpider):
    name = 'Metro'

    baseUrl = 'http://eflyer.metro.ca/MTR/MTRO/en/'
    categoryWhitelist = {'Fruit and Vegetables'}
    extractProperties = {'ProductTitle':'name', 'Price':'price'}

    def __init__(self):
        super(MetroSpider, self).__init__('NoFrills', MetroSpider.baseUrl, MetroSpider.categoryWhitelist, MetroSpider.extractProperties)