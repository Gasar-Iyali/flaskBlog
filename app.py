from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "<h1>Home Page of Zack Amata's Flask Blog</h1>Hello World. Welcome to Zack Amata's Flask Blog!"

@app.route('/zack')
def zack():
    return "Second page of Zack Amata's Flask Blog!<h1> Hi there Zack Amata</h1>"

@app.route('/about')
def about():
    return "<h1>About Page! This page tells you all about Zack Amata's Flask Blog!</h1>"


    if __name__ == '__main__':
        app.run(debug=True)