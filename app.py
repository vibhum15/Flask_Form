from flask import Flask

app = Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    return "Hello mom"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug = True)