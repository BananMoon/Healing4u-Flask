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
    
    def select(self, query):
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        
        # rows[0], rows[1]..
            # for e in rows:
        #     temp = {'user_id':e[0],'now_emotion':e[1] }
        #     ret.append(temp)
        
        self.db.commit()
        self.db.close()
        return rows

    def selectAD(self, query, data):
        self.cursor.execute(query, data)
        rows = self.cursor.fetchall()
        
        # rows[0], rows[1]..
        adData = random.choice(rows)
        adId = adData['ad_id']
        print("db_config2에서 랜덤으로 출력: ", adData)
        print("출력된 데이터의 id: ", adId )

            # for e in rows:
        #     temp = {'user_id':e[0],'now_emotion':e[1] }
        #     ret.append(temp)
        
        self.db.commit()
        self.db.close()
        return adId

    def insertUsers(self, query, data):
        self.cursor.execute(query, data)
        self.cursor.fetchall()
        print("db 업데이트 완료")

        self.db.commit()
        self.db.close()


    def selectUser(self, query):
        self.cursor.execute(query)
        userId = self.cursor.fetchall()
        print("출력된 데이터의 user id: ", userId )

        self.db.commit()
        self.db.close()
        return userId
    # def updEmp(self, empno, name, department,phone): 
    #     db = pymysql.connect(host='localhost', user='root', db='python', password='python', charset='utf8')
    #     curs = db.cursor()
        
    #     sql = "update emp set name=%s, department=%s, phone=%s where empno=%s"
    #     curs.execute(sql,(name, department, phone, empno))
    #     db.commit()
    #     db.close()
    # def delEmp(self, empno):
    #     db = pymysql.connect(host='localhost', user='root', db='python', password='python', charset='utf8')
    #     curs = db.cursor()
        
    #     sql = "delete from emp where empno=%s"
    #     curs.execute(sql,empno)
    #     db.commit()
    #     db.close()

