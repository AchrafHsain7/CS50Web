# Generated by Django 4.2.1 on 2023-06-01 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_listing_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='title',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='listing',
            name='winning_user',
            field=models.ForeignKey(blank=True, default=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_listings', to=settings.AUTH_USER_MODEL), on_delete=django.db.models.deletion.CASCADE, related_name='user_winning_listings', to=settings.AUTH_USER_MODEL),
        ),
    ]
