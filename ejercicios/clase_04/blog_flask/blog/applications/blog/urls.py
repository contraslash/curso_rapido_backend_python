from . import (
    bp,
    views,
    conf
)


def load_urls():
    bp.add_url_rule(
        "/list/",
        view_func=views.List.as_view(conf.BLOG_LIST_URL_NAME)
    )
    bp.add_url_rule(
        "/create/",
        view_func=views.Create.as_view(conf.BLOG_CREATE_URL_NAME)
    )
    bp.add_url_rule(
        "/<int:post_id>/",
        view_func=views.Detail.as_view(conf.BLOG_DETAIL_URL_NAME)
    )
