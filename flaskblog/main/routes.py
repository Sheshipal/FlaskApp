from flask import Blueprint, request, render_template
from flaskblog.models import Post

main = Blueprint('main', '__name__')

@main.route('/', methods=['GET'])
@main.route('/home', methods=['GET'])
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template("home.html", posts=posts, title='Home Page')

@main.route('/about')
def about():
    return render_template("about.html", title='About Page')