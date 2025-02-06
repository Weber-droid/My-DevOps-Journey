from flask import flask

app = Flask(__name__)

@app.route('/')
def home():
    return "This is the homepage."

if __name__ == '__main__':
    app.run()