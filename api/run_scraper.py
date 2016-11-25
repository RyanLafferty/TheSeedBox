import time, calendar

from flask import Flask
import flask_sqlalchemy


from scraper import scraper

def run_the_scrapers(nofrills=None,metro=None):

    # Set up application
    # ==========================================================================================
    application = Flask(__name__)
    application.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = True
    application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/TheSeedSA'
    #application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/TheSeed'

    db = flask_sqlalchemy.SQLAlchemy(application)

    timestamp = time.strftime('%H:%M')
    dow = list(calendar.day_abbr).index(time.strftime('%a'))

    jobs = ScraperSettings.query.filter_by(dayofweek=dow, time=timestamp)

    if nofrills is not None and metro is not None:
        scr = []
        if nofrills == "true":
            scr.add('NoFrills')
        if metro == "true":
            scr.add('Metro')

        s = scraper.Scraper(scrapers=scr)
    else:
        s = scraper.Scraper(scrapers=['NoFrills', 'Metro'])

if __name__ == "__main__":
    from seedbox import ScraperSettings
    run_the_scrapers()
