from django.contrib import admin
from django.contrib.auth.models import User, Group

from dwitter.models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    """Custom admin model. To limit which fields the Django admin should display"""
    model = User
    fields = ["username"]
    inlines = [ProfileInline]


admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.register(User, UserAdmin)
# admin.site.register(Profile)
