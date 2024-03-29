# Generated by Django 4.0.5 on 2022-08-08 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_alter_personalsmodel_p_mobile_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscribersdesiresmodel',
            name='SD_Desire',
        ),
        migrations.AddField(
            model_name='subscribersdesiresmodel',
            name='SD_Desire_first',
            field=models.CharField(choices=[('01-January____جمادى الأولى-(05)   ', '01-January__جمادى الأولى-(05)'), ('02-February___جمادى الثاني-(06)   ', '02-February_جمادى الثاني-(06)'), ('03-March______راجب-(07)           ', '03-March______________رجب-(07)'), ('04-April______شعبان-(08)          ', '04-April_____________شعبان-(08)'), ('05-May________رمضان-(09)          ', '05-May______________رمضان-(09)'), ('06-June_______شوال-(10)           ', '06-June_____________شوال-(10)'), ('07-July_______ذو القعدة-(11)      ', '07-July__________ذو القعدة-(11)'), ('08-August_____ذو الحجة-(12)       ', '08-August_______ذو الحجة-(12)'), ('09-September__محرم-(01)           ', '09-September_______محرم-(01)'), ('10-October____صفر-(02)            ', '10-October____________صفر-(02)'), ('11-November___ربيع الأول-(03)     ', '11-November___ربيع الأول-(03)'), ('12-December___ربيع الثاني-(04)    ', '12-December___ربيع الثاني-(04)'), ('لم يتم تحديد اي رغبة حتى الأن-(00)', 'لم يتم تحديد اي رغبة حتى الأن-(00)')], db_index=True, default='لم يتم تحديد اي رغبة حتى الأن-(00)', help_text='Required Field', max_length=50, verbose_name='الرغبة الأولى'),
        ),
        migrations.AddField(
            model_name='subscribersdesiresmodel',
            name='SD_Desire_second',
            field=models.CharField(choices=[('01-January____جمادى الأولى-(05)   ', '01-January__جمادى الأولى-(05)'), ('02-February___جمادى الثاني-(06)   ', '02-February_جمادى الثاني-(06)'), ('03-March______راجب-(07)           ', '03-March______________رجب-(07)'), ('04-April______شعبان-(08)          ', '04-April_____________شعبان-(08)'), ('05-May________رمضان-(09)          ', '05-May______________رمضان-(09)'), ('06-June_______شوال-(10)           ', '06-June_____________شوال-(10)'), ('07-July_______ذو القعدة-(11)      ', '07-July__________ذو القعدة-(11)'), ('08-August_____ذو الحجة-(12)       ', '08-August_______ذو الحجة-(12)'), ('09-September__محرم-(01)           ', '09-September_______محرم-(01)'), ('10-October____صفر-(02)            ', '10-October____________صفر-(02)'), ('11-November___ربيع الأول-(03)     ', '11-November___ربيع الأول-(03)'), ('12-December___ربيع الثاني-(04)    ', '12-December___ربيع الثاني-(04)'), ('لم يتم تحديد اي رغبة حتى الأن-(00)', 'لم يتم تحديد اي رغبة حتى الأن-(00)')], db_index=True, default='لم يتم تحديد اي رغبة حتى الأن-(00)', help_text='Required Field', max_length=50, verbose_name='الرغبة الثانية'),
        ),
        migrations.AddField(
            model_name='subscribersdesiresmodel',
            name='SD_Desire_third',
            field=models.CharField(choices=[('01-January____جمادى الأولى-(05)   ', '01-January__جمادى الأولى-(05)'), ('02-February___جمادى الثاني-(06)   ', '02-February_جمادى الثاني-(06)'), ('03-March______راجب-(07)           ', '03-March______________رجب-(07)'), ('04-April______شعبان-(08)          ', '04-April_____________شعبان-(08)'), ('05-May________رمضان-(09)          ', '05-May______________رمضان-(09)'), ('06-June_______شوال-(10)           ', '06-June_____________شوال-(10)'), ('07-July_______ذو القعدة-(11)      ', '07-July__________ذو القعدة-(11)'), ('08-August_____ذو الحجة-(12)       ', '08-August_______ذو الحجة-(12)'), ('09-September__محرم-(01)           ', '09-September_______محرم-(01)'), ('10-October____صفر-(02)            ', '10-October____________صفر-(02)'), ('11-November___ربيع الأول-(03)     ', '11-November___ربيع الأول-(03)'), ('12-December___ربيع الثاني-(04)    ', '12-December___ربيع الثاني-(04)'), ('لم يتم تحديد اي رغبة حتى الأن-(00)', 'لم يتم تحديد اي رغبة حتى الأن-(00)')], db_index=True, default='لم يتم تحديد اي رغبة حتى الأن-(00)', help_text='Required Field', max_length=50, verbose_name='الرغبة الثالثة'),
        ),
    ]
