import flask
import jwt
import json
import random
import mysql.connector.pooling
import time
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

PUBLIC_KEY = open("../public.key", "rb").read()
PRIVATE_KEY = open("../private.key", "rb").read()

app = flask.Flask(__name__)

dbPool = mysql.connector.pooling.MySQLConnectionPool(
  host="localhost",
  user="st-user",
  password="st-user",
  database="sinensis-test",
  pool_name="masterpool",
  pool_size=10
)


@app.route("/jwt/generate/")
def generateJwt():

  enc_jwt = jwt.encode({"nbf": 1591698124, "foo":"bar"}, PRIVATE_KEY, algorithm="RS256")
  
  resp = flask.Response(json.dumps({"status": "ok", "token": enc_jwt.decode()}))
  resp.headers["Content-Type"] = "application/json"
  return resp


@app.route("/jwt/read/")
def readJwt():
  jwt_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIiLCJuYmYiOjE1OTE2OTgxMjR9.fphVmklaDmYxaBPAvrRKA8tFqumSt5s365llP0gY1jacbzFeH52TatL8ADXu5PuKHcVtHXKKlQ0Xldf3G6vB8XqlgsFrIxb1E2td64K8nufdxelNpF9GvSxBnA3lcqt4rOh1U2Bg54O2EoFr_kFR8QcTG6uhih_6nyYmlalxxWBUmzl796g2-B0pLCreXzqxAZGBbPDvoI4V5SclAwIg5n3zo3VOQPL87ztRkBRsQZjPIFoqeRc8tBvDYtpMbhZ7XaX-CmzZt4jQYNjWKbpn02QD6NAO0tmBPTC0D4s8uFLrRT65FYk625yLAu2wHWLaV4NeWz3Boent6O1-HVfLr8D7CTtmzucd_CsWb_Zyq5kplRhCC5-LPAQj0JH_WvDSn08lcQSZ37imU8tYEPiLGLB6-u5UA4y5HqzXgI1qqdQCU8dL0o64UyuiPZD4hkv3kSgc532jD0jQq24mRWxj9GUKH1Y0wSe263Y54UEkA0RbsunRFXepsdZATVc7u3s4PPrzAmIyr-TK1pGQtBKWXkqjD0hU2dCqW7eLj61nAe3tuzXQRh9iYeSyFZsicoK6VCbRNeAfm48c_FJOGTU5KOiDRnY441_fAlTQwNqFLoRcUm1paDm0xlrCO_B68j-FGdrbaqIgF-Io20aFFNj0UEOydiGXZ89tkImzisu4i14"

  dec_jwt = jwt.decode(jwt_token, PUBLIC_KEY, algorithms='RS256')

  resp = flask.Response(json.dumps({"status": "ok", "validToken": True}))
  resp.headers["Content-Type"] = "application/json"
  return resp


@app.route("/sql/select/")
def selectSql():
  con = dbPool.get_connection()
  cursor = con.cursor(prepared=True)
  cursor.execute("SELECT age FROM readtest WHERE id = %s", (1,))
  db_resp = cursor.fetchall()
  cursor.close()

  con.close()

  resp = flask.Response(json.dumps({"status": "ok", "token": db_resp[0][0]}))
  resp.headers["Content-Type"] = "application/json"
  return resp


@app.route("/sql/insert/")
def insertSql():
  rand = random.randint(0, 100)

  con = dbPool.get_connection()
  cursor = con.cursor(prepared=True)
  cursor.execute("INSERT INTO inserttest (`number`) VALUES( %s )", (rand,))
  con.commit()
  cursor.close()

  con.close()

  resp = flask.Response(json.dumps({"status": "ok", "number": rand}))
  resp.headers["Content-Type"] = "application/json"
  return resp
