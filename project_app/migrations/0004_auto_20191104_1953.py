# Generated by Django 2.2.6 on 2019-11-04 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0003_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='full_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
