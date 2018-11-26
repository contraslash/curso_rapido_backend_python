from . import (
    bp,
    views,
    conf
)

def load_urls():
    bp.add_url_rule(
        "/log-in/",
        view_func=views.LogIn.as_view(conf.LOGIN_URL_NAME)
    )

    bp.add_url_rule(
        "/log-out/",
        view_func=views.LogOut.as_view(conf.LOGOUT_URL_NAME)
    )