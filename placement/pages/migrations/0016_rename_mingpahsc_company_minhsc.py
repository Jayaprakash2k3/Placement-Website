# Generated by Django 4.2.6 on 2023-10-16 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_company_mingpahsc_company_minsslc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='MinGPAHSC',
            new_name='MinHSC',
        ),
    ]