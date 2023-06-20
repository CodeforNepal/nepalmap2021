# Generated by Django 2.2.6 on 2022-08-08 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('description', models.TextField(default='enter content here...', verbose_name='content')),
                ('last_updated_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
