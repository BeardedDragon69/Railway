# Generated by Django 5.2 on 2025-04-07 22:11

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ticketbooking', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('issue_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('problem', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='JobRole',
            fields=[
                ('job_role_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('job_role_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Employee_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('job_role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.jobrole')),
            ],
        ),
        migrations.CreateModel(
            name='JobSchedule',
            fields=[
                ('record_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.employee')),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.issue')),
                ('train_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketbooking.train')),
            ],
        ),
        migrations.AddConstraint(
            model_name='employee',
            constraint=models.UniqueConstraint(fields=('user', 'job_role_id'), name='unique_employee'),
        ),
        migrations.AddConstraint(
            model_name='jobschedule',
            constraint=models.UniqueConstraint(fields=('train_id', 'date', 'employee'), name='unique_record'),
        ),
    ]
