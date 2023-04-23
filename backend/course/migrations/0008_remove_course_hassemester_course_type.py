# Generated by Django 4.2 on 2023-04-22 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_alter_course_hassemester'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='hasSemester',
        ),
        migrations.AddField(
            model_name='course',
            name='type',
            field=models.CharField(choices=[('SEM', 'Semester'), ('YER', 'Yearly')], default='SEM', max_length=3),
        ),
    ]