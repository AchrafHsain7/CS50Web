# Generated by Django 4.2.1 on 2023-06-01 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_alter_listing_winning_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='winning_user',
        ),
        migrations.DeleteModel(
            name='Bid',
        ),
        migrations.DeleteModel(
            name='Listing',
        ),
    ]
