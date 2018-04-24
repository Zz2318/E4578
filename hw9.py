from flask import Flask
app = Flask(__name__)

@app.route('/')
def get(): 
  quote = f.read().split('\n')
 
