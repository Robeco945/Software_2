import json
import mysql.connector
from flask import Flask, Response
app = Flask(__name__)
@app.route('/get_name/<ICAOs>')
def get_name(ICAOs):
    try:
        sql = f"select name, iso_region, municipality From  airport where ident ='{ICAOs}'"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        name = result[0][0]
        location = result[0][2]
        if cursor.rowcount > 0:
            for row in result:
                response = {
                    "ICAO": ICAOs,
                    "Name": name,
                    "Location": location
                }
                return response
    except ValueError:
        response = {
            "message": "Invalid ICAOs",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='L3ftH0me187Maria',
         autocommit=True
         )
@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")
    return http_response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)