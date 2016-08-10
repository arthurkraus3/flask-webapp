from flask import Flask
from flask import request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/db_test.db'
app.debug = True
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(255), unique=True)
    
    def __init__(self, username, email):
            self.username = username
            self.email = email
    
    def __repr__(self):
            return '<User %r>' % self.username
    

@app.route('/')
def index():
    return render_template('add_user.html')


@app.route('/post_user', methods=['POST'])
def post_user():
    user = User(request.form['username'], request.form['email'])
    user.session.add(user)
    user.session.commit()
    return redirect(url_for('index'))





app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', '8080')))

if __name__=="__main__":
    app.run()
    