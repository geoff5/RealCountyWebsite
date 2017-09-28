import DBcm

"""Contains functions for inserting, updating and retrieving data from the MySQL database"""

config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'srtb19',
    'database': 'CarlowHandball',
}

def getNews():
    sql = """select headline, filename from news
            order by newsID desc limit 3"""
    stories = []
    
    with DBcm.UseDatabase(config) as database:
        database.execute(sql)
        stories = database.fetchall()
    return stories
         