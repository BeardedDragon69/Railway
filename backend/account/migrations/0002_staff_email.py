# Generated by Django 5.2 on 2025-04-07 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='staff_email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_email', models.EmailField(max_length=255, unique=True)),
            ],
        ),
    ]
