from flask import Flask

app = Flask(__name__)

@app.route('/')
def me():
    return "hello ttyf"

if __name__ == '__main__':
    app.run()