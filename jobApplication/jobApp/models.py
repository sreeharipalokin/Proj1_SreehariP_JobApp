from django.db import models

# Create your models here.
class ApplicantDetails(models.Model):
    full_name = models.CharField(max_length=75)
    country_code = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=10, unique=True)
    email_id = models.EmailField(max_length=254, unique=True)
    dob = models.DateField()
    gender = models.CharField(max_length=7)
    years = models.CharField(max_length=2)
    months = models.CharField(max_length=2)
    job_role = models.CharField(max_length=30)
    address_line_1 = models.CharField(max_length=200)
    address_line_2 = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=7)

    def __str__(self):
        return self.full_name
    