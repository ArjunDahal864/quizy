# Generated by Django 4.2 on 2023-04-22 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mcq', '0004_question_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=5000, verbose_name='option')),
                ('is_correct', models.BooleanField(default=False, verbose_name='is_correct')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mcq.question')),
            ],
        ),
    ]
