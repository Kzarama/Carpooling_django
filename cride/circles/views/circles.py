from rest_framework import viewsets

from cride.circles.serializers import CircleModelSerializer

from cride.circles.models import Circle

class CircleViewSet(viewsets.ModelViewSet):
    queryset = Circle.objects.all()
    serializer_class = CircleModelSerializer