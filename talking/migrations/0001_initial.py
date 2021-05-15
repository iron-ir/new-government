# Generated by Django 3.2 on 2021-05-15 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('off_on', models.BooleanField(default=False)),
                ('employees', models.ManyToManyField(related_name='t_u_employees', to=settings.AUTH_USER_MODEL)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='t_u_owner', to=settings.AUTH_USER_MODEL, verbose_name='مالک')),
            ],
            options={
                'verbose_name': 'مباحثه عمومی',
                'verbose_name_plural': 'مباحثات عمومی',
            },
        ),
        migrations.CreateModel(
            name='ShortMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_time', models.DateTimeField(verbose_name='زمان ارسال')),
                ('text', models.TextField(blank=True, null=True, verbose_name='متن')),
                ('file', models.FilePathField(blank=True, null=True, verbose_name='فایل')),
                ('send', models.BooleanField(default=False, verbose_name='ارسال شد')),
                ('received', models.BooleanField(default=False, verbose_name='دریافت شد')),
                ('read', models.BooleanField(default=False, verbose_name='خوانده شد')),
                ('presentable', models.BooleanField(default=True, verbose_name='قابل نمایش')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u_sm_receiver', to='talking.talk', verbose_name='دریافت کننده')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u_sm_sender', to=settings.AUTH_USER_MODEL, verbose_name='ارسال کننده')),
            ],
        ),
    ]