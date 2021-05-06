from django.apps import AppConfig


class BaseInformationSettingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_information_settings'
    verbose_name = 'تنظیمات مربوط به اطلاعات پایه'

