from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class UserAdminConfig(UserAdmin):

    search_fields = ('username', 'email', 'date_of_birth',)
    list_filter = ('username', 'email', 'date_of_birth',
                   'is_active', 'is_hosting', 'is_online')
    ordering = ('-date_joined',)
    list_display = ('username', 'email', 'date_of_birth',
                    'is_active', 'is_hosting', 'is_online', 'date_joined', 'last_login',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'date_of_birth',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active',)}),
        ('Personal', {'fields': ('user_bio', 'user_icon')}),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'date_of_birth', 'password1', 'password2', 'is_active', 'is_staff',),

        }),

    )


admin.site.register(UserProfile, UserAdminConfig)
