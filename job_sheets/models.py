from django.db import models

class Client(models.Model):
    client_id = models.CharField(max_length=100, unique=True)
    client_name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=15)
    received_date = models.DateField()
    inventory_received = models.CharField(max_length=100)
    reported_issues = models.TextField()
    client_notes = models.TextField(blank=True, null=True)
    assigned_technician = models.CharField(max_length=100)
    estimated_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    deadline = models.DateField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('in-progress', 'In Progress'), ('completed', 'Completed')])

    def __str__(self):
        return self.client_name

# Create your models here.
