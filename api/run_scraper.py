import time, calendar

from flask import Flask
import flask_sqlalchemy

from seedbox import ScraperSettings

from scraper import scraper

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

s = scraper.Scraper(['NoFrills', 'Metro'])
