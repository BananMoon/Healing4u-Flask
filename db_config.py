import pymysql
import random

class healingDao:
    def __init__(self):
        self.db = pymysql.connect(
            host= 'healing.ceuy4iegap9i.ap-northeast-2.rds.amazonaws.com',
            user= 'healing4u',
            password= 'healing4u',
            db= 'healingDB',
            charset='utf8'
        )
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def selectAD(self, query, data):
        self.cursor.execute(query, data)
        rows = self.cursor.fetchall()
        
        # rows[0], rows[1]..
        adData = random.choice(rows)
        adId = adData['ad_id']
        print("db_config2에서 랜덤으로 출력: ", adData)
        print("출력된 데이터의 id: ", adId )
        
        self.db.commit()
        # self.db.close()
        return adId

    def insertUsers(self, query, data):
        self.cursor.execute(query, data)
        self.cursor.fetchall()
        print("db 업데이트 완료")

        self.db.commit()
        # self.db.close()


    def selectUser(self, query):
        self.cursor.execute(query)
        row = self.cursor.fetchall()
        print(row)
        userId = row[0]['user_id']
        print("출력된 데이터의 user id: ", userId )

        self.db.commit()
        self.db.close()
        return userId