from rest_framework import viewsets, mixins

from rest_framework.permissions import IsAuthenticated
from cride.circles.permissions.circles import IsCircleAdmin

from cride.circles.serializers import CircleModelSerializer

from cride.circles.models import Circle, Membership

class CircleViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):

    serializer_class = CircleModelSerializer

    def get_queryset(self):
        """restrict list to public only"""
        queryset = Circle.objects.all()
        if self.action == 'list':
            return queryset.filter(is_public=True)
        return queryset
    
    def get_permissions(self):
        """Assign permission based on action"""
        permissions = [IsAuthenticated]
        if self.action in ['update', 'partial_update']:
            permission.append(IsCircleAdmin)
        return [permission() for permission in permissions]

    def perform_create(self, serializer):
        """Assign circle admin."""
        circle = serializer.save()
        user = self.request.user
        profile = user.profile
        Membership.objects.create(
            user=user,
            profile=profile,
            circle=circle,
            is_admin=True,
            remaining_invitations=10
        )