# Generated by Django 2.0.5 on 2018-07-05 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuId', models.CharField(max_length=50)),
                ('choice', models.IntegerField()),
                ('blank', models.IntegerField()),
                ('q17', models.IntegerField()),
                ('q18', models.IntegerField()),
                ('q19', models.IntegerField()),
                ('q20', models.IntegerField()),
                ('q21', models.IntegerField()),
                ('q22', models.IntegerField()),
                ('q23', models.IntegerField()),
                ('q24', models.IntegerField()),
                ('q25', models.IntegerField()),
                ('q26', models.IntegerField()),
                ('q27', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
        ),
    ]
