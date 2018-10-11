SURVEY_PREFIX_URL = "survey"

SURVEY_LIST_URL_NAME = "survey_list"
SURVEY_CREATE_URL_NAME = "survey_create"
SURVEY_DETAIL_URL_NAME = "survey_detail"
SURVEY_UPDATE_URL_NAME = "survey_update"
SURVEY_DELETE_URL_NAME = "survey_delete"

def get_prefixed_url(url):
    return "{}.{}".format(SURVEY_PREFIX_URL, url)