# Generated by Django 5.0.3 on 2024-05-10 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_teacher_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='price_list',
        ),
    ]
