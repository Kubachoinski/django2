from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class UserAdminClass(UserAdmin):
   fieldsets = (
       (None, {
           'fields': ('username', 'password')
       }),
       ('Personal info', {
           'fields': ('first_name', 'last_name', 'email')
       }),
       ('Permissions', {
           'fields': (
               'is_active', 'is_staff', 'is_superuser', 'role',
               'groups', 'user_permissions'
           )
       }),
       ('Important dates', {
           'fields': ('last_login', 'date_joined')
       }),
   )


admin.site.register(User, UserAdminClass)