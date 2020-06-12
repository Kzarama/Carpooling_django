from rest_framework.decorators import api_view
from rest_framework.response import Response

from cride.circles.models import Circle

@api_view(['GET'])
def list_circles(request):
    circles = Circle.objects.filter(is_public=True)
    data = []
    for circle in circles:
        data.append({
            'name':circle.name,
            'slug_name':circle.slug_name,
            'rides_taken':circle.rides_taken,
            'rides_offered':circle.rides_offered,
            'members_limit':circle.members_limit,
        })
    return Response(data)

@api_view(['POST'])
def create_circle(request):
    name = request.data['name']
    slug_name = request.data['slug_name']
    about = request.data.get('about',  '')
    circle = Circle.objects.create(name=name, slug_name=slug_name, about=about)
    data = {
        'name':circle.name,
        'slug_name':circle.slug_name,
        'rides_taken':circle.rides_taken,
        'rides_offered':circle.rides_offered,
        'members_limit':circle.members_limit,
    }
    return Response(data)