# Generated by Django 4.1.7 on 2023-08-07 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0007_coinnews_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='coinnews',
            name='create_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
