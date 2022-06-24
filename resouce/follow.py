



from importlib.resources import Resource
from sre_constants import SUCCESS

from flask import request


class FollowResource(Resource) :
    @jwt_required()
    def post(self, follow_id) :

        #1. 클라이언트로부터 데이터를 받아온다.
        offset = request.args['offset']
        limit = request_args['limit']

        user_id = get_jwt_identity()

        get_jwt_identity()

        #2. 데이터베이스에 친구정보 인서트한다.
         try :
            # 데이터 insert 
            # 1. DB에 연결
            connection = get_connection()

            # 2. 쿼리문 만들기
            query = '''insert into memo
                    (title, date, content, user_id)
                    values
                    (%s , %s ,);'''
            
            record = (data['title'], data['date'], 
                    data['content'], user_id  )

            # 3. 커서를 가져온다.
            cursor = connection.cursor()

            # 4. 쿼리문을 커서를 이용해서 실행한다.
            cursor.execute(query, record)

            # 5. 커넥션을 커밋해줘야 한다 => 디비에 영구적으로 반영하라는 뜻
            connection.commit()

            # 6. 자원 해제
            cursor.close()
            connection.close()

        except mysql.connector.Error as e :
            print(e)
            cursor.close()
            connection.close()
            return {"error" : str(e)}, 503


        
        return  {result : success} , 200

class FollowResource(Resource) :
    @jwt_required()
    def get(self) :
        return



        