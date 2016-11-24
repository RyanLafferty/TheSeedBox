# -*- coding: utf-8 -*-

import re
from scrapy.exceptions import DropItem

class ProductPipeline(object):
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
        #TODO Submit post requests to insert products
        result = self.parse_price(item['price'])
        if result:
            item['quantity'], item['price'] = result
        else:
            raise DropItem("Unable to parse item's price: %s" % item['price'])

        print item
        return item
