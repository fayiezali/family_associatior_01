# Generated by Django 4.0.5 on 2022-08-05 15:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0011_alter_personalsmodel_p_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalsmodel',
            name='P_User',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='اسم المشترك'),
            preserve_default=False,
        ),
    ]
