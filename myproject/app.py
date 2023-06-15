from flask import Flask, render_template, request, flash, redirect, url_for
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('data.sqlite', check_same_thread=False)

if __name__ == '__main__':
    app.run(debug=True, port=8001)
posts = [
    {
        'author': 'Giga Bin',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'May 29, 2023'
    },
    {
        'author': 'Ilolia Yasou',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'May 30, 2023'
    }
]


@app.route("/")
def hello_world():
    return render_template('main.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data_post = request.form
        username = data_post['username']
        email = data_post['email']
        password = data_post['password']
        sqlAddAccount = "INSERT INTO account (username,email,password) VALUES('"+str(
            username)+"','"+str(email)+"','"+str(password)+"')"
        conn.execute(sqlAddAccount)
        conn.commit()
        return redirect("/")
    return render_template('register.html')


# @app.route("/login")
# def login():
#     form = LoginForm()
#     return render_template('login.html', title='Login', form=form)
