# Generated by Django 3.1.1 on 2020-09-21 07:01

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
import scraping.models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0002_error'),
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_data', jsonfield.fields.JSONField(default=scraping.models.default_urls)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.city', verbose_name='Город')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.language', verbose_name='Язык программирования')),
            ],
            options={
                'unique_together': {('city', 'language')},
            },
        ),
    ]
