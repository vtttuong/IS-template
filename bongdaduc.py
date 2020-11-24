import scrapy
from scrapy import Request
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
import urllib
import json
import datetime
import sqlite3
from sqlite3 import Error
    

class bongdaducSpider(scrapy.Spider):
    name = 'bongdaduc'

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'bongdaduc.csv'
    }
    def __init__(self, conn):
        self.conn = conn

    def start_requests(self):
        for i in range(1, 34 + 1):
            url = 'https://bongda24h.vn/services/bongda24h.svc/getFootballSchedules2/4,12,{},id,aid,pid,vs,wl,k'.format(i)
            yield scrapy.Request(
                url= url,
                method='GET',
                callback=self.parse_page
            ) 
    def parse_page(self, response):
        data = json.loads(response.body)
        roundItem = {}
        value =[]
        value.append(data['list'][0]['RoundId'])
        roundItem['Round'] = data['list'][0]['RoundId']
        for match in data['list'][0]['l_Matches']:
            value =[]
            roundItem['Round'] = data['list'][0]['RoundId']
            roundItem['AwayName'] = match['AwayName']
            roundItem['AwayGoals'] = match['AwayGoals']
            roundItem['HomeName'] = match['HomeName']
            roundItem['HomeGoals'] = match['HomeGoals']
            roundItem['StadiumName'] = match['StadiumName']
            roundItem['StartDate'] = match['StartDate']
            roundItem['StartTime'] = match['StartTime']
            value.append(match['AwayName'])
            value.append(match['AwayGoals'])
            value.append(match['HomeName'])
            value.append(match['HomeGoals'])
            value.append(match['StadiumName'])
            value.append(match['StartDate'])
            value.append(match['StartTime'])
            
            sql = ''' INSERT INTO bundesliga_schedule_2020
                (
                    round, 
                    awayname, 
                    awaygoals, 
                    homename, 
                    homegoals, 
                    stadiumname, 
                    startdate, 
                    starttime
                )
                VALUES(?,?,?,?,?,?,?,?) '''
                
            cur = self.conn.cursor()
            cur.execute(sql, value)
            self.conn.commit()
            # yield roundItem


if __name__ == '__main__':
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(r"C:\Users\DELL\Desktop\MLAPLI-master\app\mpgWebApp\db.sqlite3")

        process = CrawlerProcess()
        process.crawl(bongdaducSpider, conn)
        process.start()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    