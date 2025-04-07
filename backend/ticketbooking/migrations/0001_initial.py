# Generated by Django 5.2 on 2025-04-07 22:11

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('coach_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('coach_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('train_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('train_name', models.CharField(max_length=50)),
                ('train_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('seat_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('seat_type', models.CharField(max_length=50)),
                ('seat_number', models.CharField(max_length=10)),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketbooking.coach')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticket_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('schedule_id', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('booked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketbooking.coach')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketbooking.passenger')),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketbooking.seat')),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketbooking.train')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comments', models.TextField()),
                ('rating', models.PositiveSmallIntegerField()),
                ('passenger_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('train_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketbooking.train')),
            ],
        ),
        migrations.AddField(
            model_name='coach',
            name='train',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketbooking.train'),
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reservation_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('reservation_date', models.DateField()),
                ('created_at', models.DateField(auto_now=True)),
                ('booked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tickets', models.ManyToManyField(to='ticketbooking.ticket')),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('reservation_id',), name='unique_reservation')],
            },
        ),
        migrations.AddConstraint(
            model_name='ticket',
            constraint=models.UniqueConstraint(fields=('seat', 'date', 'train', 'coach'), name='unique_seat'),
        ),
        migrations.AddConstraint(
            model_name='review',
            constraint=models.CheckConstraint(condition=models.Q(('rating__gte', 1), ('rating__lte', 5)), name='valid_rating_range'),
        ),
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(fields=('passenger_id', 'train_id'), name='unique_review'),
        ),
    ]
