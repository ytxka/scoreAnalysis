# Generated by Django 2.0.5 on 2018-07-05 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreSubmit', '0002_statistic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='bzc',
            field=models.FloatField(),
        ),
    ]
