from django.db import models
from django.contrib.auth.models import User

from patient import models as pmodels
from donor import models as dmodels
class Stock(models.Model):
    bloodgroup=models.CharField(max_length=10)
    unit=models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.bloodgroup

class BloodRequest(models.Model):
    request_by_patient=models.ForeignKey(pmodels.Patient,null=True,on_delete=models.CASCADE)
    request_by_donor=models.ForeignKey(dmodels.Donor,null=True,on_delete=models.CASCADE)
    patient_name=models.CharField(max_length=30)
    patient_age=models.PositiveIntegerField()
    reason=models.CharField(max_length=500)
    bloodgroup=models.CharField(max_length=10)
    unit=models.PositiveIntegerField(default=0)
    status=models.CharField(max_length=20,default="Pending")
    date=models.DateField(auto_now=True)
    def __str__(self):
        return self.bloodgroup

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patients')
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    sugar_level = models.DecimalField(max_digits=5, decimal_places=2)
    medicine = models.TextField()
    other_details = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.phone_number}"