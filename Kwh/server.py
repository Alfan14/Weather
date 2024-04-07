from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

from flask import Flask, render_template, request
from waitress import serve

app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/call-python-function') 
def call_python_function(): 
    # Your Python function code here 
    return {'result': 'success'} 

if  __name__ == "__main__":
    serve(app,host="0.0.0.0", port=8000)
