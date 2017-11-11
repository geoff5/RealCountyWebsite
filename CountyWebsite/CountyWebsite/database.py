import DBcm
import datetime

"""Contains functions for inserting, updating and retrieving data from the MySQL database"""

config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'srtb19',
    'database': 'CarlowHandball',
}

def getHeadline(id):
    sql = """SELECT headline, FROM news  
            WHERE newsID = %s"""    

    with DBcm.UseDatabase(config) as database:
        database.execute(sql, (id))
        rows = database.fetchall()
    
    return rows[0][0]    

def getHomepageNews():
    sql = """SELECT headline, paragraph FROM news
            ORDER BY newsID DESC LIMIT 3"""
    stories = []
    
    with DBcm.UseDatabase(config) as database:
        database.execute(sql)
        stories = database.fetchall()
    return stories

def getNewsID():
    sql = """SELECT id WHERE news
            ORDER BY newsID DESC LIMIT 1"""
    stories = []
    
    with DBcm.UseDatabase(config) as database:
        database.execute(sql)
        stories = database.fetchall()
    id = stories[0][0]
    return id

def addNews(story):
    date = datetime.datetime.now()
    id = getNewsID()    

    sql = """INSERT INTO news
          (id, headline, createdOn, createdBy, filename)
          values
          (%s, %s, %s, %s, %s, %s)"""
    with DBcm.UseDatabase(config) as database:
        database.execute(sql, (id, story['headline'], date, story['author'], story['filename']))

def addPlayer(player):
    sql = """INSERT INTO players
            (firstname,lastname,email,phonenumber,club,username,password,isboardmember,approved)
            values
            (%s,%s,%s,%s,%s,%s,%s,0,0)"""

    with DBcm.UseDatabase(config) as database:
        database.execute(sql, (player['firstname'],player['lastname'],player['email'],player['phonenumber'],player['club'],player['username'],player['password']))