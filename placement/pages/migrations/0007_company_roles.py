# Generated by Django 4.2.6 on 2023-10-16 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_student_batch_student_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='roles',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]