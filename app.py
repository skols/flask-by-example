from flask import Flask
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

@app.route('/')
def hello():
    return "Hello world!"

@app.route('/<name>/')
def hello_name(name):
    return "Hello {}!".format(name)
    
if __name__ == '__main__':
    host = os.getenv('IP','0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.run(host=host, port=port)
