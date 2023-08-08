from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'username': 'Aisha'}
    posts = [
        {
            'author': {'username': 'Aisha'},
            'body': 'Beautiful day in Kenya!'
        },
        {
            'author': {'username': 'Khalfan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
