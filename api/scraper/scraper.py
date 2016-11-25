from scrapy.crawler import CrawlerProcess
from grocer.spiders.nofrills import NoFrillsSpider
from grocer.spiders.metro import MetroSpider
from scrapy.utils.project import get_project_settings

class Scraper:
    def execute(self, spiders):
        spiderDefns = {'Metro': MetroSpider, 'NoFrills': NoFrillsSpider}

        print get_project_settings().attributes['ITEM_PIPELINES'].value.attributes.keys()

        process = CrawlerProcess(get_project_settings())

        for spider in spiders:
            if spider in spiderDefns:
                process.crawl(spiderDefns[spider])

        process.start()