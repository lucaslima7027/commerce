# Generated by Django 4.2.6 on 2023-10-26 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Watch_List',
            new_name='UserWL',
        ),
    ]
