from flask import Flask
from flask import render_template
from database import get_all_cats, create_cat, get_cat

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)

@app.route('/cats/<int:id>')
def cat_profile(id):
    # TODO: read cat  by id
    cat=get_cat(id)
    return render_template(
        'cat.html', cat=cat)

@app.route('/add_cat')
def new_cat():
    return render_template(
        'add.html')


if __name__ == '__main__':
   app.run(debug = True)
