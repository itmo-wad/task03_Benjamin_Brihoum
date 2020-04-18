from app import app
from flask import render_template, request, redirect, abort, request, flash, url_for
from flask_login import LoginManager, logout_user, login_required, login_user


login_manager = LoginManager()
login_manager.init_app(app)

usr = ""

@app.route('/cabinet')
def index():
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
@login_manager.user_loader
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' or request.form['password'] == 'admin':
            flash('Logged in successfully.')
            next = request.args.get('next')
            #login_user(request.form["username"], remember=True)
            return redirect(next or url_for('index'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html')


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')
