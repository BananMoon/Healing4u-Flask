import pymysql

class Database():
    def __init__(self):
        self.db = pymysql.connect(
            host= 'healing.ceuy4iegap9i.ap-northeast-2.rds.amazonaws.com',
            user= 'healing4u',
            password= 'healing4u',
            db= 'healingDB',
            charset='utf8'
        )
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def insert(self, query, args=)

    def execute(self, query, args={}):
        self.cursor.execute(query, args)
    
    def executeOne(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()
        return row
    
    def executeAll(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row

    def commit():
        db.commit()


# DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"