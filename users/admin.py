from django.contrib import admin
from .models import *


@admin.register(Privacy)
class PrivacyAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkExpiration)
class WorkExpirationAdmin(admin.ModelAdmin):
    pass


@admin.register(EducationHistory)
class EducationHistoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Standpoint)
class StandpointAdmin(admin.ModelAdmin):
    pass


@admin.register(Effect)
class EffectAdmin(admin.ModelAdmin):
    pass


@admin.register(UserRelation)
class UserRelationAdmin(admin.ModelAdmin):
    pass


admin.site.site_header = "ادمین سایت رفراندوم"
admin.site.site_title = "پرتال ادمین"
admin.site.index_title = "به پرتال ادمین سایت رفراندوم خوش آمدید."
