from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Article

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'date_of_birth')
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Article)
