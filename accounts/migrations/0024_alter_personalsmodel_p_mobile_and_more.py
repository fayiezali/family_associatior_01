# Generated by Django 4.0.5 on 2022-08-07 21:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0023_alter_personalsmodel_p_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalsmodel',
            name='P_Mobile',
            field=phonenumber_field.modelfields.PhoneNumberField(db_index=True, default='+966555555555', max_length=128, region=None, verbose_name='الجوال'),
        ),
        migrations.CreateModel(
            name='SubscribersDesiresMODEL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SD_Desire', models.CharField(choices=[('01-January____جمادى الأولى-(05)   ', '01-January__جمادى الأولى-(05)'), ('02-February___جمادى الثاني-(06)   ', '02-February_جمادى الثاني-(06)'), ('03-March______راجب-(07)           ', '03-March______________رجب-(07)'), ('04-April______شعبان-(08)          ', '04-April_____________شعبان-(08)'), ('05-May________رمضان-(09)          ', '05-May______________رمضان-(09)'), ('06-June_______شوال-(10)           ', '06-June_____________شوال-(10)'), ('07-July_______ذو القعدة-(11)      ', '07-July__________ذو القعدة-(11)'), ('08-August_____ذو الحجة-(12)       ', '08-August_______ذو الحجة-(12)'), ('09-September__محرم-(01)           ', '09-September_______محرم-(01)'), ('10-October____صفر-(02)            ', '10-October____________صفر-(02)'), ('11-November___ربيع الأول-(03)     ', '11-November___ربيع الأول-(03)'), ('12-December___ربيع الثاني-(04)    ', '12-December___ربيع الثاني-(04)'), ('لم يتم تحديد اي رغبة حتى الأن-(00)', 'لم يتم تحديد اي رغبة حتى الأن-(00)')], db_index=True, default='لم يتم تحديد اي رغبة حتى الأن-(00)', help_text='Required Field', max_length=50, verbose_name='الرغبة')),
                ('SD_Notes', models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='الملاحظات')),
                ('SD_User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='اسم المشترك')),
            ],
            options={
                'verbose_name_plural': 'Subscribers Desires',
            },
        ),
    ]
