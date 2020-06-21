from django.contrib import admin

from cride.circles.models import Circle


@admin.register(Circle)
class CircleAdmin(admin.ModelAdmin):
    list_display = ('slug_name', 'name', 'is_public', 'verified', 'is_limited', 'members_limit')
    search_fields = ('slug_name', 'name')
    list_filter = ('is_public', 'verified', 'is_limited')

    actions = ['make_verified', 'make_unverified']

    def make_verified(self, request, queryset):
        """Make circles verified"""
        queryset.update(verified=True)
    
    make_verified.short_description = 'Make selected circles verified'

    def make_unverified(self, request, queryset):
        """Make circles unverified"""
        queryset.update(verified=False)
    
    make_unverified.short_description = 'Make selected circles unverified'