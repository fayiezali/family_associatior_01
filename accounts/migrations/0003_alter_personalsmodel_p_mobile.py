# Generated by Django 4.0.5 on 2022-07-26 06:44

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_personalsmodel_p_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalsmodel',
            name='P_Mobile',
            field=phonenumber_field.modelfields.PhoneNumberField(db_index=True, max_length=128, region=None, verbose_name='الجوال'),
        ),
    ]
