# Generated by Django 3.2 on 2022-09-24 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MaybornApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Holiday_1', models.SmallIntegerField()),
                ('Holiday_2', models.SmallIntegerField()),
                ('Holiday_3', models.SmallIntegerField()),
                ('Holiday_4', models.SmallIntegerField()),
                ('Holiday_5', models.SmallIntegerField()),
                ('Holiday_6', models.SmallIntegerField()),
                ('Holiday_7', models.SmallIntegerField()),
                ('Holiday_8', models.SmallIntegerField()),
                ('Holiday_9', models.SmallIntegerField()),
                ('Holiday_10', models.SmallIntegerField()),
                ('Comments', models.CharField(max_length=500)),
            ],
        ),
    ]