from flask_restful import fields
from flask_restful.reqparse import RequestParser

post_parser = RequestParser()
post_parser.add_argument(
    'title',
    dest='title',
    location='form',
    required=True
)
post_parser.add_argument(
    'body',
    dest='body',
    location='form',
    required=True
)

post_fields = {
    "id": fields.Integer,
    "title": fields.String,
    "body": fields.String,
    "pub_date": fields.DateTime
}
