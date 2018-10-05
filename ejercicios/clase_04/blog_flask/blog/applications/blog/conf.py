BLOG_PREFIX_URL = "blog"

BLOG_LIST_URL_NAME = "blog_list"
BLOG_CREATE_URL_NAME = "blog_create"

def get_prefixed_url(url):
    return "{}.{}".format(BLOG_PREFIX_URL, url)