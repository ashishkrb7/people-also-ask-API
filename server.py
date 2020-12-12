"""
.  .     .               .   .                                   .
|\ |     |               |   |                                   |             o  ,- o
| \| ,-: |-  . . ;-. ,-: |   | ,-: ;-. ,-: . . ,-: ,-: ,-.   ,-. | ,-: ,-. ,-. .  |  . ,-. ;-.
|  | | | |   | | |   | | |   | | | | | | | | | | | | | |-'   |   | | | `-. `-. |  |- | |-' |
'  ' `-` `-' `-` '   `-` '   ' `-` ' ' `-| `-` `-` `-| `-'   `-' ' `-` `-' `-' '  |  ' `-' '
                                       `-'         `-'                           -'
"""

from flask import Flask,request
import pandas as pd
import json
import src
app = Flask(__name__)
 
@app.route('/Request', methods = ['POST','GET'])
def RequestHandler():
    """ method to predict commitment """
    content = request.get_json()
    Data=pd.DataFrame([content])
    try:
        output=src.main(Data,filename="Request")
    except:
        output=[]
    return(output)

app.run(host='0.0.0.0', port= 80,debug=True,threaded=True)