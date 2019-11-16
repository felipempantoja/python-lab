from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/<int:id>')
def find(id):
    return 'id is %d' % id

if __name__ == '__main__':
    app.run(host='0.0.0.0')
