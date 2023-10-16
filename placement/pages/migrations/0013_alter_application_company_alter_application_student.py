# Generated by Django 4.2.6 on 2023-10-16 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_alter_application_company_alter_application_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='company',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='pages.company'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='student',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='pages.student'),
            preserve_default=False,
        ),
    ]
