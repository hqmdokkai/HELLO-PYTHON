from flask import Flask

app = Flask('Hello')

@app.route('/')
def hello_world():
  return 'Hello, Python'

app.run(host='0.0.0.0', port=8080)
