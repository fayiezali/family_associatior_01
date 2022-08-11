# Generated by Django 4.0.5 on 2022-08-06 15:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0018_alter_profile_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalsmodel',
            name='P_Mobile',
            field=phonenumber_field.modelfields.PhoneNumberField(db_index=True, max_length=128, region=None, unique=True, verbose_name='الجوال'),
        ),
        migrations.AlterField(
            model_name='personalsmodel',
            name='P_User',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='اسم المشترك'),
        ),
    ]