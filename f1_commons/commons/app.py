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
            }

#ENDPOINTS
api.add_resource(DefaultRoute, '/')


if __name__ == "__main__":
    app.run(debug=True)