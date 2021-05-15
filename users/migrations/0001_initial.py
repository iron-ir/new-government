# Generated by Django 3.2 on 2021-05-15 14:38

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import repository.regular_expression
import repository.uploader


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base_information_settings', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('_is_verify', models.BooleanField(default=False, verbose_name='تایید')),
                ('is_personal_information_verify', models.BooleanField(default=False, verbose_name='تایید اطلاعات شخصی')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='ایمیل')),
                ('is_email_verify', models.BooleanField(default=False, verbose_name='تایید ایمیل')),
                ('phone_number', models.CharField(blank=True, max_length=16, null=True, unique=True, validators=[repository.regular_expression.UnicodePhoneNumberValidator()], verbose_name='شماره تلفن')),
                ('is_phone_number_verify', models.BooleanField(default=False, verbose_name='تایید شماره تلفن')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=repository.uploader.image_upload_to, verbose_name='عکس پروفایل')),
                ('first_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='نام')),
                ('last_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='نام خانوادگی')),
                ('_gender', models.CharField(choices=[('0', 'خالی'), ('1', 'خانوم'), ('2', 'آقا'), ('3', 'دیگر')], default='0', max_length=1, verbose_name='جنسیت')),
                ('national_code', models.CharField(blank=True, max_length=16, null=True, unique=True, validators=[repository.regular_expression.UnicodeNationalcodeValidator()], verbose_name='کد ملی')),
                ('father_name', models.CharField(blank=True, max_length=32, null=True, verbose_name='نام پدر')),
                ('mother_name', models.CharField(blank=True, max_length=32, null=True, verbose_name='نام مادر')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='تاریخ تولد')),
                ('official_website', models.URLField(blank=True, null=True, unique=True, verbose_name='وب سایت رسمی')),
                ('birth_place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_information_settings.zone', verbose_name='محل تولد')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('nationality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bi_c_nationality', to='base_information_settings.baseinformation', verbose_name='ملیت')),
                ('religion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bi_c_religion', to='base_information_settings.baseinformation', verbose_name='دین')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربران',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='VCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('string', models.CharField(editable=False, max_length=5, verbose_name='کد')),
                ('_vctype', models.CharField(choices=[('0', 'شماره تلفن'), ('1', 'ایمیل')], editable=False, max_length=2, verbose_name='نوع')),
                ('expiration_date', models.DateTimeField(editable=False, verbose_name='تاریخ انقضا')),
                ('used', models.BooleanField(blank=True, editable=False, null=True, verbose_name='استفاده شده')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'کد تایید',
                'verbose_name_plural': 'کدهای تایید',
            },
        ),
        migrations.CreateModel(
            name='WorkExpiration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_number_for_sorting', models.IntegerField(blank=True, null=True, verbose_name='شماره مرتب سازی')),
                ('is_verify', models.BooleanField(default=False, verbose_name='تایید')),
                ('post_title', models.CharField(max_length=64, verbose_name='عنوان جایگاه')),
                ('from_date', models.DateField(blank=True, null=True, verbose_name='از تاریخ')),
                ('to_date', models.DateField(blank=True, null=True, verbose_name='تا تاریخ')),
                ('organization_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='نام سازمان')),
                ('activity_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bi_we_activity_type', to='base_information_settings.baseinformation', verbose_name='نوع فعالیت')),
                ('cooperation_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bi_we_cooperation_type', to='base_information_settings.baseinformation', verbose_name='نوع همکاری')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'سابقه کاری',
                'verbose_name_plural': 'سوابق کاری',
                'unique_together': {('place_number_for_sorting', 'user')},
            },
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date_time', models.DateTimeField(verbose_name='از')),
                ('to_date_time', models.DateTimeField(verbose_name='تا')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_information_settings.role', verbose_name='نقش')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'نقش کاربر',
                'verbose_name_plural': 'نقش های کاربران',
                'unique_together': {('user', 'role')},
            },
        ),
        migrations.CreateModel(
            name='UserRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_is_verify', models.BooleanField(default=False, verbose_name='تایید رابطه')),
                ('base_user_verification', models.BooleanField(blank=True, null=True, verbose_name='تایید رابطه توسط کاربر پایه')),
                ('related_user_verification', models.BooleanField(blank=True, null=True, verbose_name='تایید رابطه توسط کاربر مرتبط')),
                ('form_date', models.DateField(blank=True, null=True, verbose_name='شروع رابطه')),
                ('to_date', models.DateField(blank=True, null=True, verbose_name='اتمام رابطه')),
                ('base_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u_ur_base_user', to=settings.AUTH_USER_MODEL, verbose_name='نامزد')),
                ('related_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u_ur_related_user', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
                ('rtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_information_settings.baseinformation', verbose_name='نوع رابطه')),
            ],
            options={
                'verbose_name': 'رابطه فرد',
                'verbose_name_plural': 'روابط افراد',
                'unique_together': {('base_user', 'related_user')},
            },
        ),
        migrations.CreateModel(
            name='Standpoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_number_for_sorting', models.IntegerField(blank=True, null=True, verbose_name='شماره مرتب سازی')),
                ('title', models.CharField(max_length=128, verbose_name='عنوان')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال')),
                ('link', models.URLField(blank=True, null=True, verbose_name='لینک')),
                ('attachment', models.FileField(blank=True, null=True, upload_to=repository.uploader.file_upload_to, verbose_name='پیوست')),
                ('group', models.ForeignKey(help_text='این دیدگاه مربوط به کدام دسته بندی -مثلا دسته بندی سیاست خارجی، امور اجتماعی و ...-است.', on_delete=django.db.models.deletion.CASCADE, to='base_information_settings.baseinformation', verbose_name='دسته بندی')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نامزد')),
            ],
            options={
                'verbose_name': 'دیدگاه',
                'verbose_name_plural': 'دیدگاه ها',
                'unique_together': {('place_number_for_sorting', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Effect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_number_for_sorting', models.IntegerField(blank=True, null=True, verbose_name='شماره مرتب سازی')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال')),
                ('title', models.CharField(max_length=128, verbose_name='عنوان')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('link', models.URLField(blank=True, null=True, verbose_name='لینک')),
                ('attachment', models.FileField(blank=True, null=True, upload_to=repository.uploader.file_upload_to, verbose_name='پیوست')),
                ('etype', models.ForeignKey(help_text='این اثر از چه نوعی - کتاب، مقاله، فیلم و ...- است.', on_delete=django.db.models.deletion.CASCADE, to='base_information_settings.baseinformation', verbose_name='نوغ')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'اثر',
                'verbose_name_plural': 'آثار',
                'unique_together': {('place_number_for_sorting', 'user')},
            },
        ),
        migrations.CreateModel(
            name='EducationHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_number_for_sorting', models.IntegerField(blank=True, null=True, verbose_name='شماره مرتب سازی')),
                ('is_verify', models.BooleanField(default=False, verbose_name='تایید')),
                ('place_of_study', models.CharField(max_length=64, verbose_name='نام موسسه')),
                ('graduation_date', models.DateField(blank=True, null=True, verbose_name='تاریخ اخذ مدرک')),
                ('is_study', models.BooleanField(default=False, verbose_name='در حال تحصیل')),
                ('degree_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bi_eh_degree_type', to='base_information_settings.baseinformation', verbose_name='مقطع')),
                ('field_of_study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bi_eh_field_of_study', to='base_information_settings.baseinformation', verbose_name='رشته')),
                ('place_of_study_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bi_eh_place_of_study_type', to='base_information_settings.baseinformation', verbose_name='نوع موسسه')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_information_settings.zone', verbose_name='مکان')),
            ],
            options={
                'verbose_name': 'سابقه تحصیلی',
                'verbose_name_plural': 'سوابق تحصیلی',
                'unique_together': {('place_number_for_sorting', 'user')},
            },
        ),
    ]
