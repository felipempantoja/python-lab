from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/<int:id>')
def find(id):
    return 'id is %d' % id
