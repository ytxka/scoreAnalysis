# Generated by Django 2.0.5 on 2018-07-08 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('knowledgePoint', '0005_auto_20180708_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zsdth',
            name='kpId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='knowledgePoint.zsd'),
        ),
    ]