# Generated by Django 2.2.6 on 2019-11-17 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0006_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='slug',
            field=models.SlugField(max_length=104, null=True),
        ),
    ]
