# Generated by Django 4.1.7 on 2023-08-11 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0008_coinnews_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='coinnews',
            name='source_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='coinnews',
            name='tickers',
            field=models.TextField(blank=True, null=True),
        ),
    ]