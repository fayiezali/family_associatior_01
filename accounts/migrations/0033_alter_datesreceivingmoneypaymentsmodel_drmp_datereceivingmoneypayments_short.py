# Generated by Django 4.0.5 on 2022-08-13 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0032_alter_datesreceivingmoneypaymentsmodel_drmp_notes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datesreceivingmoneypaymentsmodel',
            name='DRMP_DateReceivingMoneyPayments_Short',
            field=models.DateField(blank=True, db_index=True, default='0000-00-00', help_text='Required Field', null=True, verbose_name='موعد إستلام المال - بالتاريخ'),
        ),
    ]
