# Generated by Django 5.2 on 2025-04-07 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketbooking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='destination',
            field=models.CharField(default='lorem', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='starting_point',
            field=models.CharField(default='lorem', max_length=50),
            preserve_default=False,
        ),
    ]
