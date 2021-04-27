from flask import Flask, render_template, url_for, session, redirect, request
from client import Client

NAME_KEY = 'name'
app = Flask(__name__)
app.secret_key = 'hellomynameissteveandyouwontguessthis'


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session[NAME_KEY] = request.form['inputName']
        return redirect(url_for('home'))
    return render_template('login.html', **{'session': session})


@app.route('/logout')
def logout():
    session.pop(NAME_KEY, None)
    return redirect(url_for('login'))


@app.route("/")
@app.route("/home")
def home():
    if NAME_KEY not in session:
        return redirect(url_for('login'))

    return render_template("index.html", **{"login": True, "session": session})


@app.route('/run', method=['GET'])
def run(url=None):
    msg = request.args.get('val')
    print(msg)
    return 'none'


if __name__ == '__main__':
    app.run(debug=True)
