# Generated by Django 5.0.3 on 2024-05-25 08:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='favorite_students',
            field=models.ManyToManyField(related_name='favorite_students', to=settings.AUTH_USER_MODEL),
        ),
    ]
