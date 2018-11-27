AUTH_PREFIX_URL = "auth"

LOGIN_URL_NAME = "log_in"
LOGOUT_URL_NAME = "log_out"


def get_prefixed_url(url):
    return "{}:{}".format(AUTH_PREFIX_URL, url)
