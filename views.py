from flask import Flask, render_template
from main import app
from models import Post, User, Role


@app.route('/')
def index():
    # return render_template(
    #     'home.html'
    # )
    return '<h1>Hello!</h1>'


@app.route('/<int:page>')
def home(page=1):
    posts = Post.query.order_by(
        Post.publish_date.desc()
    ).paginate(page, 10)

    return  render_template(
        'home.html',
        posts=posts
    )


@app.route
def login():
    pass


@app.route
def logout():
    pass


@app.route
def register():
    pass
