import csv

from flask_restful import Resource, marshal_with
from flask import request
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

class PostSubir(Resource):
    @marshal_with(serializers.post_fields)
    def post(self):
        print(request.files)
        archivo = request.files.get("archivo")
        # readed_file = archivo.read().decode()
        # print(archivo.readlines())
        binary_lines = archivo.readlines()
        decoded_lines = [line.decode() for line in binary_lines]
        posts  = list()
        reader = csv.reader(decoded_lines)
        # Skip first line
        next(reader)
        for r in reader:
            post = models.Post(
                title=r[0],
                body=r[1]
            )
            posts.append(post)
            models.db.session.add(post)

        models.db.session.commit()

        # Manually open csv file
        # print(archivo)
        # print(readed_file)
        # lineas = readed_file.split("\n")
        # posts  = list()
        # for i ,linea in enumerate(lineas):
        #     if i > 0:
        #         valores = linea.split(",")
        #         print(valores)
        #         post = models.Post(
        #             title=valores[0],
        #             body=valores[1]
        #         )
        #         posts.append(post)
        #         models.db.session.add(post)
        #
        # models.db.session.commit()

        return posts