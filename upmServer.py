from flask import Flask
from flask import request
from flask import jsonify
from flask import redirect,url_for
import json
import time

app = Flask(__name__)

@app.route("/login")
def login():
    return "Hello World!"

@app.route("/")
def hello():
    return  redirect(url_for('login'))


@app.route("/upm/households")
def upmResponse():
    print request.method
    limit = request.args.get('limit',0)
    offset = request.args.get('offset',0)
    total=request.args.get('total',True)

    jsdat = open("UPM-Household.txt")
    dat = json.load(jsdat)
    dat['start'] = int(offset)
    subs = dat['body']    
    
    sub1 = subs[0]
    for i in range(int(limit)-1):        
        sub2 = sub1.copy()
        hh = sub2['householdId']
        hh = hh+"_"+str(i)
        sub2['householdId']=hh
        subs.append(sub2)
    
    print limit

#    time.sleep(2)
    
    return jsonify(dat)

if __name__ == "__main__":
    app.debug =  True
    app.run(host="0.0.0.0", port=9999)
