import os
from sanic import Sanic
from sanic.response import json
import mysql.connector


try:
    cnx = mysql.connector.connect(
        host=os.environ["DB_HOST"],
        port=os.environ["DB_PORT"],
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASS"])
    cursor = cnx.cursor()
except Exception as e:
    print("Error connecting to database {}".format(e))


app = Sanic(name='Link Shorterner')







if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ["SERVER_PORT"])
    cursor.close()
    cnx.close()
