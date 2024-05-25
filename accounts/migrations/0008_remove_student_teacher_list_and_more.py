# Generated by Django 5.0.3 on 2024-05-24 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_user_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teacher_list',
        ),
        migrations.AddField(
            model_name='student',
            name='favorite_teachers',
            field=models.ManyToManyField(related_name='favorite_teachers', to='accounts.teacher'),
        ),
    ]