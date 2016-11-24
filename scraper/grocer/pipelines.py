# -*- coding: utf-8 -*-
import re, requests, time
from scrapy.exceptions import DropItem

class ProductPipeline(object):
    def __init__(self):
        self.date = time.strftime("%Y-%m-%dT%H:%M:%S")

    def parse_price(self, value):
        match = re.match('^(\d+)\/\$([-+]?[0-9]*\.?[0-9]+)$', value)
        if match:
            return int(match.group(1)), float(match.group(2))

        match = re.match('^(\d+)\/([-+]?[0-9]*\.?[0-9]+)¢$', value)
        if match:
            return int(match.group(1)), float(match.group(2)) / 100

        match = re.match('^\$([-+]?[0-9]*\.?[0-9]+)$', value)
        if match:
            return 1, float(match.group(1))

        match = re.match('^([-+]?[0-9]*\.?[0-9]+)¢$', value)
        if match:
            return 1, float(match.group(1)) / 100

        return False

    def process_item(self, item, spider):
        result = self.parse_price(item['price'])

        if result:
            item['quantity'], item['price'] = result
        else:
            raise DropItem("Unable to parse item's price: %s" % item['price'])

        item['source'] = spider.name
        item['dateCreated'] = self.date

        response = requests.post('http://localhost:5000/api/Products', json=dict(item))

        return item