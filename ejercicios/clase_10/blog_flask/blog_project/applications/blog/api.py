from flask_restful import Resource, marshal_with

from . import (
    models,
    serializers
)


class Post(Resource):
    @marshal_with(serializers.post_fields)
    def get(self):
        print(models.Post.query.all())
        return models.Post.query.all()

    @marshal_with(serializers.post_fields)
    def post(self):
        args = serializers.post_parser.parse_args()
        print(args)
        post = models.Post(
            title=args.title,
            body=args.body
        )
        models.db.session.add(post)
        models.db.session.commit()
        return post

class PostWithId(Resource):

    @marshal_with(serializers.post_fields)
    def get(self, id):
        print(models.Post.query.all())
        return models.Post.query.filter_by(id=id).first_or_404()



    @marshal_with(serializers.post_fields)
    def put(self, id):
        args = serializers.post_parser.parse_args()
        post = models.Post.query.filter_by(id=id).first_or_404()
        post.title = args.title
        post.body = args.body
        models.db.session.add(post)
        models.db.session.commit()
        return post

    def delete(self, id):
        models.Post.query.filter_by(id=id).delete()
        models.db.session.commit()
        return {"status": "deleted"}
