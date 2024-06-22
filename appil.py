from flask import Flask
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq

app  = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hellow, world!</h1>"

if __name__=="main__":
    app.run(degub=Flase, host="0.0.0.0")