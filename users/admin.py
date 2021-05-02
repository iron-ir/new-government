from django.contrib import admin
from .models import User, Candidate, WorkExpiration


# @admin.register(UserRole)
# class UserRoleAdmin(admin.ModelAdmin):
#     list_display = ('user', 'role', 'from_date_time', 'to_date_time')
#     list_filter = ('user', 'role',)
#     search_fields = ['user', 'role', ]
#
#
# @admin.register(Role)
# class RoleAdmin(admin.ModelAdmin):
#     list_display = ('title', 'is_active',)
#     list_filter = ('title', 'is_active',)
#     search_fields = ['title', ]
#
#
@admin.register(WorkExpiration)
class WorkExpirationAdmin(admin.ModelAdmin):
    list_display = ('user', 'post_title', 'organization_name',)
    list_filter = ('user', 'post_title', 'organization_name',)
    search_fields = ['user', 'post_title', 'organization_name', ]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_staff', 'phone_number',)
    list_filter = ('is_staff', 'is_active',)
    search_fields = ['username', 'phone_number', ]
    fieldsets = [(
        'اطلاعات ورود به سامانه', {
            'fields': [
                'username',
                'password',
            ]
        }
    ), (
        'اطلاعات فردی', {
            'fields': [
                'avatar',
                'email',
                'phone_number',
            ]
        }
    ), (
        'اطلاعات تکمیلی مربوط به سامانه', {
            'fields': [
                'is_staff',
                'is_active',
                'date_joined',
                'last_login',
                'groups',
            ]
        }
    ),
    ]

    def save_model(self, request, obj, form, change):
        from django.contrib.auth.hashers import make_password
        obj.password = make_password(request.POST['password'])
        super().save_model(request, obj, form, change)


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('national_code', 'first_name', 'last_name',)
    search_fields = ['national_code', ]
    fieldsets = [(
        'اطلاعات فردی', {
            'fields': [
                'national_code',
                ('first_name', 'last_name'),
                'father_name',
                'birth_date',
            ]
        }
    ),
    ]

# admin.site.site_header = "ادمین"
# admin.site.site_title = "پرتال ادمین"
# admin.site.index_title = "به پرتال ادمین خوش آمدید."
