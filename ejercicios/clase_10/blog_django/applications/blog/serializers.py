from rest_framework import serializers

from . import models

class Post(serializers.ModelSerializer):

    class Meta:
        model = models.Post
        fields = (
            'id',
            'title',
            'body'
        )
