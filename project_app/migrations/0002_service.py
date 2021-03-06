# Generated by Django 2.2.6 on 2019-10-27 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Service Title')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'ACTIVE'), (1, 'INACTIVE'), (2, 'DELETED')], default=0)),
                ('price', models.PositiveIntegerField(blank=True, default=0)),
            ],
        ),
    ]
