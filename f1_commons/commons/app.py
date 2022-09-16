from flask import Flask, request
from flask_restful import  Resource, Api, reqparse
import sql_connection
import platform

app = Flask(__name__)
api = Api(app)
db_conn = sql_connection.create_server_connection()

class DefaultRoute(Resource):
    def get(self):
        return {
            'Current_OS':     platform.system(),
            'OS_information': platform.version(),
            'my_sql_version': sql_connection.get_info(db_conn)
            }, 200


class Users(Resource):
    def get(self):
        sql_query = 'SELECT * FROM Users;'
        if db_conn:
            result = sql_connection.read_query(db_conn, sql_query)
            return result, 200
        else:
            return "No results found check database"
    def post_new_user(self):
        pass

#ENDPOINTS
api.add_resource(DefaultRoute, '/')
api.add_resource(Users, '/users')


if __name__ == "__main__":
    app.run(debug=False)