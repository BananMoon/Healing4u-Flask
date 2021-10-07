from flask import Flask, render_template, jsonify

import pymysql
import datetime
# import db_config
import db_config2
# HTML 파일을 렌더링할 때 추가적으로 필요한 파일들을 static이라는 디렉터리에 넣겠다.
app = Flask(__name__, static_url_path="/static")


@app.route('/')
def index():
    return render_template('index.html')

# SELECT 함수 예제
# @app.route('/select', methods=['GET'])
# def select():
#     conn = db_config.Database()
 
#     sql     = "SELECT user_id, now_emotion \
#                 FROM users"
#     row     = conn.executeAll(sql)
 
#     print(row)
 
#     return render_template('test.html',
#                             result=None,
#                             resultData=row[0],
#                             resultUPDATE=None)

@app.route('/select', methods=['GET'])
def select():
    conn = db_config2.healingDao()
 
    query     = "SELECT user_id, now_emotion FROM `users`"
    row     = conn.select(query)
 
    print("server에서 출력: ",row[0]['user_id']);
    # row : [{'user_id': 2, 'now_emotion': 0}, {'user_id': 3, 'now_emotion': 1}, {'user_id': 4, 'now_emotion': 0}, {'user_id': 5, 'now_emotion': 0}]

    return render_template('test.html',
                            result=None,
                            resultData=row[0],
                            resultUPDATE=None)


@app.route('/test', methods=['GET'])
def insert():
    conn = db_config2.healingDao()
    
    # 1. 광고데이터 랜덤으로 추출
    ## (1) 오늘의 월
    dt_m = datetime.datetime.now().month
    print(dt_m)

    if (3<=dt_m & dt_m<=5):
        season_param = 0    #봄
    elif (6<=dt_m & dt_m<=8):
        season_param = 1    #여름
    elif (9<=dt_m & dt_m<=11):
        season_param = 2    #가을
    else:
        season_param = 3    #겨울
    
    ## (2) season&now_emotion으로 광고데이터 랜덤 추출
    select_data = (0, season_param)  # emotion에 now_emotion값 넣어야함
    select_query = "SELECT * FROM `advertisement` WHERE emotion=%s AND season=%s;"  

    ad_id = conn.selectAD(select_query, select_data)   #랜덤으로 뽑힌 ad_id만 return받으면 됨

    # 2. userID 값 1씩 증가시켜서 생성.
    #  
    # 3. 감정값 받아들이기 form 모델
    # Q. socket통신해서 값있냐? 물어보고
    # (1) 그 값을 result로 받으면 전달 가능
    # (2) 변수 자체를 인식못할수도...


    # 4. users 테이블에 userID, 감정값, 광고ID 를 insert
    # insert_data=(user_id, now_emotion, ad_id)     # ex) (5,2,16)

    # insert_query = "INSERT INTO `users` (user_id, now_emotion, ad_id) VALUES (%s, %s, %s)"
    
    # conn.insert(insert_query, insert_data)

    # 추가) 가장 최근의 필드를 꺼내서 그거의 user_id를 웹서버에 전송
    # SELECT * FROM users ORDER BY user_id DESC LIMIT 1;


    # 5. user_id, now_emotion, ad_id 웹서버로 전송
    return jsonify({
        'user_id': 5,
        'now_emotion': 0,
        'ad_id': ad_id
    })


if __name__ == "__main__":
    app.run(debug=True)

