# Generated by Django 4.1.7 on 2023-07-31 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0004_alter_coinnews_options_alter_coinnews_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coinnews',
            options={'managed': True},
        ),
        migrations.AlterModelTable(
            name='coinnews',
            table='coin_news',
        ),
    ]
