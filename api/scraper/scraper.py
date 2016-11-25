from scrapy.crawler import CrawlerProcess
from grocer.spiders.nofrills import NoFrillsSpider
from grocer.spiders.metro import MetroSpider
from scrapy.utils.project import get_project_settings

class Scraper:
    spiderDefns = {}

    def __init__(self, scrapers=None):
        if scrapers is None:
            self.spiderDefns = { 'Metro': MetroSpider, 'NoFrills': NoFrillsSpider }

        if "Metro" in scrapers:
            self.spiderDefns['Metro'] = MetroSpider

        if "NoFrills" in scrapers:
            self.spiderDefns['Metro'] = NoFrillsSpider

    def execute(self, spiders):
        print get_project_settings().attributes['ITEM_PIPELINES'].value.attributes.keys()

        process = CrawlerProcess(get_project_settings())

        for spider in spiders:
            if spider in self.spiderDefns:
                process.crawl(self.spiderDefns[spider])

        process.start()
