from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import rides as ride_views

router = DefaultRouter()
router.register(
    r'circles/(?P<slug_name>[-a-zA-Z0-9_]+)/rides',
    ride_views.RideViewSet,
    basename='ride'
)

urlpatterns = [
    path('', include(router.urls))
]
