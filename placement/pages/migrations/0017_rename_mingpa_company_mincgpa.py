# Generated by Django 4.2.6 on 2023-10-16 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_rename_mingpahsc_company_minhsc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='MinGPA',
            new_name='MinCGPA',
        ),
    ]
