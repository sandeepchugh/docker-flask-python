from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

# https://stackoverflow.com/questions/26423984/unable-to-connect-to-flask-app-on-docker-from-host
if __name__ == '__main__':
    app.run(host='0.0.0.0')
