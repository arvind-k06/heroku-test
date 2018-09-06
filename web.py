from flask import Flask
app = Flask(__name__)

@app.rouye('/')
def index():
  return 'hello heroku'
