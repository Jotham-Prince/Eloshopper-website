# Generated by Django 4.1 on 2022-09-27 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('term_title', models.CharField(default='terms title', max_length=400)),
                ('term_description', models.TextField(default='terms and conditions...')),
                ('policy', models.CharField(default='policy footer', max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'Subscribers',
                'db_table': 'subscribers',
            },
        ),
    ]
