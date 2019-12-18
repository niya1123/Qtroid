from flask import Flask

import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world!!"

@app.route('/api/registerMySQL')
def api_registermySQL():
    subprocess.check_call(['python','qtroid.py'])
    return "Hello api world!!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)