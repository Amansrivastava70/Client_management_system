# Generated by Django 5.0.6 on 2024-09-17 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(max_length=100, unique=True)),
                ('client_name', models.CharField(max_length=100)),
                ('contact_info', models.CharField(max_length=15)),
                ('received_date', models.DateField()),
                ('inventory_received', models.CharField(max_length=100)),
                ('reported_issues', models.TextField()),
                ('client_notes', models.TextField(blank=True, null=True)),
                ('assigned_technician', models.CharField(max_length=100)),
                ('estimated_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('deadline', models.DateField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('in-progress', 'In Progress'), ('completed', 'Completed')], max_length=20)),
            ],
        ),
    ]
