from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from cride.circles.models import Circle

class CircleSerializer(serializers.Serializer):
    name = serializers.CharField()
    slug_name = serializers.SlugField()
    rides_taken = serializers.IntegerField()
    rides_offered = serializers.IntegerField()
    members_limit = serializers.IntegerField()

class CreateCircleSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=140)
    slug_name = serializers.SlugField(max_length=40)
    about = serializers.CharField(max_length=255, 
        required=False,
        validators=[UniqueValidator(queryset=Circle.objects.all())]
    )

    def create(self, data):
        return Circle.objects.create(**data)