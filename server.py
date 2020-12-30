#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask,request,jsonify
from src.Engine import search
import json

app = Flask(__name__)

@app.route('/PAA', methods = ['POST','GET'])
def main():
    """ Web service for getting people also ask from google (with some customization) """
    try:
        content = request.get_json()
        Result=json.dumps({"PAA":search(content.get("q"),int(content.get("n")-1))})
    except:
        Result=json.dumps({"PAA" : ""})
    return(Result)

if __name__=="__main__":
    app.run(debug=True)
