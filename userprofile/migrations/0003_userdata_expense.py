# Generated by Django 3.2.10 on 2022-08-05 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_remove_userdata_total_expense'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='expense',
            field=models.BigIntegerField(default=0),
        ),
    ]
