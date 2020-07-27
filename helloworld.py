from flask import Flask 
from flask import request 

app = Flask(__name__) 

@app.route('/main') 
def main_page(): 
    return "Hello Flask!" 

if __name__ == '__main__': 
    app.run(port=5550)
