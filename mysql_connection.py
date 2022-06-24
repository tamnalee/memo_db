import mysql.connector
def get_connection():
    connection = mysql.connector.connect(
    host = 'yh-db.~~~.ap-northeast-2.rds.amazonaws.com',  # sql 호스트네임 작성
    database = 'recipe_db',
    user = 'recipe_user',  # SQL 에서 작성한 레시피 앱 사용자 계정
    password = 'recipe1234'
 )
    return connection

    import mysql.connector
from mysql_connection import get_connection

class RecipeListResource(Resource):
    # restful api의 method에 해당하는 함수 작성 (실행이 되는 프레임워크 콜백함수)
    def post(self):
        # api 실행코드를 작성

        # 클라이언트에서 body부분에 작성한 json을 받아오는 코드 
        data = request.get_json()

        try:s
            pass

        except mysql.connector.Error as e:
            pass
    return
    