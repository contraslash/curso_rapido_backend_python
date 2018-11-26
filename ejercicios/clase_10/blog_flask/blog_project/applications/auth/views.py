from flask.views import View
from flask.templating import render_template
from flask.helpers import url_for, request, flash
from flask.globals import g
from flask_login import login_user, logout_user
from werkzeug.utils import redirect

from . import (
    conf,
    models
)

class LogIn(View):
    methods = ["GET", "POST"]
    def dispatch_request(self):
        context = dict()
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            registered_user = models.User.query.filter_by(username=username, password=password).first()
            if registered_user is None:
                flash('Username or Password is invalid', 'error')
                return redirect(
                    url_for(
                        request.args.get('next') or
                        conf.get_prefixed_url(
                            conf.LOGIN_URL_NAME
                        )
                    )
                )
            login_user(registered_user)
            flash('Logged in successfully')
            return redirect("/")
        return render_template('log_in.html', **context)


class LogOut(View):

    def dispatch_request(self):
        logout_user()
        flash('Logged out successfully')
        return redirect("/")