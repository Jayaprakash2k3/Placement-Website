# Generated by Django 4.2.6 on 2023-10-16 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_rename_mingpa_company_mincgpa'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='isPR',
            field=models.BooleanField(default=False),
        ),
    ]