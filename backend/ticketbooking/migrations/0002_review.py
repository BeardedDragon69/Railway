# Generated by Django 5.2 on 2025-04-07 08:21

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketbooking', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='review',
            fields=[
                ('review_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comments', models.TextField()),
                ('rating', models.PositiveSmallIntegerField()),
                ('passenger_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('train_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketbooking.train')),
            ],
            options={
                'constraints': [models.CheckConstraint(condition=models.Q(('rating__gte', 1), ('rating__lte', 5)), name='valid_rating_range')],
            },
        ),
    ]
