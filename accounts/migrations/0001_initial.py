# Generated by Django 4.0.5 on 2022-07-03 22:26

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
            name='PersonalsMODEL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('P_Avialable', models.BooleanField(db_index=True, default=True, verbose_name='حالة المشترك_نشط')),
                ('slug', models.SlugField(blank=True, verbose_name='الإسم التعريفي')),
                ('P_FirstName', models.CharField(db_index=True, max_length=50, verbose_name='الإسم الأول')),
                ('P_FatherName', models.CharField(db_index=True, max_length=50, verbose_name='إسم الاب')),
                ('P_GrandFatherName', models.CharField(db_index=True, max_length=50, verbose_name='إسم الجد')),
                ('P_FamilyName', models.CharField(db_index=True, max_length=50, verbose_name='إسم العائلة')),
                ('P_Photo', models.ImageField(db_index=True, default='Default_Image.png', upload_to='PersonaFile_Photo/', verbose_name='الصورة الشخصية')),
                ('P_Mobile', models.CharField(db_index=True, max_length=10, verbose_name='الجوال')),
                ('P_Address', models.CharField(db_index=True, max_length=100, verbose_name='العنوان')),
                ('P_Notes', models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='الملاحظات')),
                ('P_User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='اسم المشترك')),
            ],
            options={
                'ordering': ['P_User'],
            },
        ),
        migrations.CreateModel(
            name='FinancialStatementsMODEL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FS_SubscriptionAmount', models.DecimalField(db_index=True, decimal_places=2, default=50, max_digits=8, verbose_name='مبلغ الإشتراك')),
                ('FS_NumberPaymentsDue', models.IntegerField(db_index=True, default=1, verbose_name='عدد الدفعات')),
                ('FS_BankName', models.CharField(db_index=True, max_length=50, verbose_name='إسم البنك')),
                ('FS_BankAccount', models.CharField(db_index=True, max_length=50, verbose_name='الحساب البنكي - الآيبان')),
                ('FS_Notes', models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='الملاحظات')),
                ('FS_User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='اسم المشترك')),
            ],
            options={
                'ordering': ['FS_User'],
            },
        ),
        migrations.CreateModel(
            name='DatesReceivingMoneyPaymentsMODEL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DRMP_DateReceivingMoneyPayments_Long', models.CharField(choices=[('01-January__Jumada Al-Awwal-(05)', '01-January__Jumada Al-Awwal-(05)'), ('02-February_Jumada Al-Thani-(06)', '02-February_Jumada Al-Thani-(06)'), ('03-March______________Rajab-(07)', '03-March______________Rajab-(07)'), ('04-April_____________Shaban-(08)', '04-April_____________Shaban-(08)'), ('05-May______________Ramadan-(09)', '05-May______________Ramadan-(09)'), ('06-June_____________Shawwal-(10)', '06-June_____________Shawwal-(10)'), ('07-July__________Dhul-Qadah-(11)', '07-July__________Dhul-Qadah-(11)'), ('08-August_______Dhul-Hijjah-(12)', '08-August_______Dhul-Hijjah-(12)'), ('09-September_______Muharram-(01)', '09-September_______Muharram-(01)'), ('10-October____________Safar-(02)', '10-October____________Safar-(02)'), ('11-November___Rabi Al-Awwal-(03)', '11-November___Rabi Al-Awwal-(03)'), ('12-December___Rabi Al-Thani-(04)', '12-December___Rabi Al-Thani-(04)'), ('00-All_______________Al-Kol-(00)', '00-All_______________Al-Kol-(00)')], db_index=True, default='Please Choose', help_text='Required Field', max_length=50, verbose_name='موعد إستلام المال - بالشهر')),
                ('DRMP_DateReceivingMoneyPayments_Short', models.DateField(blank=True, db_index=True, help_text='Required Field', null=True, verbose_name='موعد إستلام المال - بالتاريخ')),
                ('DRMP_Notes', models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='الملاحظات')),
                ('DRMP_User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='اسم المشترك')),
            ],
            options={
                'ordering': ['DRMP_DateReceivingMoneyPayments_Short'],
            },
        ),
    ]
