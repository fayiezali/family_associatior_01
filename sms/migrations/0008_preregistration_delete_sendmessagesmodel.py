# Generated by Django 4.0.5 on 2022-07-16 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0007_alter_sendmessagesmodel_sm_mobil'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password1', models.CharField(max_length=100)),
                ('password2', models.CharField(max_length=100)),
                ('otp', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='SendMessagesMODEL',
        ),
    ]