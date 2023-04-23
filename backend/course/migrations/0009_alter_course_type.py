# Generated by Django 4.2 on 2023-04-22 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_remove_course_hassemester_course_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='type',
            field=models.CharField(choices=[('SEM', 'Sem'), ('YER', 'Yer')], default='SEM', max_length=3),
        ),
    ]