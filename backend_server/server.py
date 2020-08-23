import os
from sanic import Sanic
from sanic.response import json,redirect
import mysql.connector
from link_generator import generator
from time import sleep

app = Sanic(name='Link Shorterner')

base_path = os.environ["SERVER_ADDR"]

@app.route("/link/",methods=["POST"])
def link_shortener(req):
    '''
    Entrypoint to get and generate a persistent shortened link.
    :args: link:string
    '''
    if req.method == "POST":
        try:

            link = req.args["link"][0]
            shortened_link = generator(link)
            cursor.execute("INSERT INTO data(`shortened_link`,`link`) VALUES(%s, %s)", (shortened_link, link))
            cnx.commit()
            return json({"success":True,"link":base_path+ '/' +shortened_link})

        except Exception as e:
            return json({"success":False,"error":e})
    else:
        return json({"success":False,"error":"Method not supported"})

@app.route('/<link:string>',methods=["GET"])
def link_redirect(req,link):
    '''
    Redirects user if the link is valid (ie in the database)
    :args: link:string
    '''
    try:
        cursor.execute("SELECT `link` from `data` WHERE `shortened_link` = %s", (link,))
        res = cursor.fetchone()[0]
        if res:
            print(res)
            return redirect(res)
    except Exception as e:
        return json({"success":False,"error":e})

if __name__ == "__main__":
    cursor = None
    while cursor is None:
        try:
            cnx = mysql.connector.connect(
                host=os.environ["DB_HOST"],
                port=os.environ["DB_PORT"],
                database=os.environ["DB_NAME"],
                user=os.environ["DB_USER"],
                password=os.environ["DB_PASS"])
            cursor = cnx.cursor()
            print("Connected!")
        except Exception as e:
            print("Error connecting to database {} Retrying...".format(e))
            sleep(2)
            cursor = None


    app.run(host="0.0.0.0", port=os.environ["SERVER_PORT"])
    cursor.close()
    cnx.close()
