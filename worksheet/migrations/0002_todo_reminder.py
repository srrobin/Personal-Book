# Generated by Django 2.2.3 on 2019-07-23 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worksheet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='reminder',
            field=models.TimeField(null=True),
        ),
    ]
