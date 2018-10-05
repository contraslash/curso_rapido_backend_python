from flask.views import View
from flask.templating import render_template
from flask.helpers import url_for, request, flash
from flask.globals import g
from werkzeug.utils import redirect

from . import (
    conf,
    models
)

class List(View):

    def dispatch_request(self):
        context = dict()
        context["posts"] = models.Post.query.all()

        return render_template('list.html', **context)



class Create(View):
    methods = ["GET", "POST"]
    def dispatch_request(self):
        if request.method == 'POST':
            title = request.form['title']
            body = request.form['body']
            error = None

            if not title:
                error = 'Title is required.'

            if error is not None:
                flash(error)
            else:
                post = models.Post(
                    title=title,
                    body=body
                )
                models.db.session.add(post)
                models.db.session.commit()
                return redirect(
                    url_for(
                        conf.get_prefixed_url(conf.BLOG_LIST_URL_NAME)
                    )
                )
        return render_template('create.html')