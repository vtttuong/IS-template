import scrapy
from scrapy import Request
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
import urllib
import json
import datetime
import sqlite3
from sqlite3 import Error
    

class bongdaanhSpider(scrapy.Spider):
    name = 'bongdaanh'

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'bongdaanh.csv'
    }
    base_url = 'https://coupler.foxsports.com.au/api/v1/scorecentre/sports/football/series/21/seasons/132/scorecards.json'

    def __init__(self, leagueId):
        # self.conn = conn
        self.leagueId = leagueId
        
    def start_requests(self):
        for i in range(1, 38 + 1):
            querry_params = '?channelSize=1&masthead=foxsports&roundId={}&statsApiEnv=prod&statsApiKey=A00239D3-45F6-4A0A-810C-54A347F144C2'.format(i)
            yield scrapy.Request(
                url= self.base_url + querry_params,
                method='GET',
                callback=self.parse_link,
            ) 

    def parse_link(self, response):
        match_list = json.loads(response.body)
        for match in match_list:
            matchItem = {}
            matchItem['Series'] = match['series']['name']
            matchItem['Season'] = match['season']['year']
            matchItem['Round'] = match['round']['number']
            matchItem['HomeName'] = match['team_A']['name']
            matchItem['HomeLogo'] = 'https://content.foxsports.com.au/fs/match-centre/team-logo/football/{}.png'.format(match['team_A']['id'])
            matchItem['HomeGoals'] = match['team_A']['score']
            matchItem['AwayName'] = match['team_B']['name']
            matchItem['AwayLogo'] = 'https://content.foxsports.com.au/fs/match-centre/team-logo/football/{}.png'.format(match['team_B']['id'])
            matchItem['AwayGoals'] = match['team_B']['score']
            matchItem['StadiumName'] = match['venue']['name']
            matchItem['StartDate'] = match['match_start_date']
            yield matchItem

if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(bongdaanhSpider, 1)
    process.start()
