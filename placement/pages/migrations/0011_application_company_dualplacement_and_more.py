# Generated by Django 4.2.6 on 2023-10-16 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_alter_student_placedin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='dualPlacement',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='StudentApplication',
        ),
        migrations.AddField(
            model_name='application',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.company'),
        ),
        migrations.AddField(
            model_name='application',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.student'),
        ),
    ]
