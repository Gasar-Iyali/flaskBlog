from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World. Welcome to Zack Amata's Flask Blog!"

@app.route('/zack')
def zack():
    return "Second page of Zack Amata's Flask Blog!"


    if __name__ == '__main__':
        app.run(debug=True)