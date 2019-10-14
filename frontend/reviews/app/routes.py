from flask import render_template
from app import app, models, mongo



@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/check')
def check():
    example = models.Reviews.query.all()
    print(example)
    return f'<h1> {example}<h1>'

@app.route("/home")
def home_page():
    online_users = mongo.db.users.find({"online": True})
    print(online_users)
    return f"<h1> {online_users} <h1>"
