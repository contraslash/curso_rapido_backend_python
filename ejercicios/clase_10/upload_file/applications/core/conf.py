CORE_PREFIX = "core"

FILE_UPLOAD = "file_upload"


def get_prefixed_url(url):
    return "{}:{}".format(CORE_PREFIX, url)
