from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config()

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/mypage')
def mypage():
    return 'THis is a page!'

if __name__ == '__main__':
    app.run(debug=True,port=8000)
    
    
    