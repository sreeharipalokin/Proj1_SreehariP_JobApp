from django.db import models

# Create your models here.
class ApplicantDetails(models.Model):
    full_name = models.CharField(max_length = 75)
    country_code = models.CharField(max_length = 3)
    phone_number = models.CharField(max_length = 10, unique=True)
    email_id = models.EmailField(max_length = 254, unique=True)
    dob = models.DateField()
    gender = models.CharField(max_length = 7, null = True)
    years = models.CharField(max_length = 2, null = True)
    months = models.CharField(max_length = 2, null = True)
    job_role = models.CharField(max_length = 30)
    address_line_1 = models.CharField(max_length = 200, null = True)
    address_line_2 = models.CharField(max_length = 100, null = True)
    city = models.CharField(max_length = 30, null = True)
    state = models.CharField(max_length = 30, null = True)
    country = models.CharField(max_length = 30, null = True)
    zip_code = models.CharField(max_length = 7, null = True)

    def __str__(self):
        return self.full_name
    
class ApplicantDetailsModel(models.Model):
    full_name = models.CharField(max_length = 75)
    country_code_choices = [
        ("+91", "+91"),
        ("+1", "+1"),
    ]
    country_code = models.CharField(max_length = 3, choices = country_code_choices, default = "+91")
    phone_number = models.CharField(max_length = 10, unique=True)
    email_id = models.EmailField(max_length = 254, unique=True)
    dob = models.DateField()
    gender_choices = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Others", "Others"),
    ]
    gender = models.CharField(max_length = 7, null = True, choices = gender_choices, default = None)
    years_choices = [
        ("", "Years"),
        ("0", "Fresher"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("9+", "9+"),
    ]
    years = models.CharField(max_length = 2, null = True, choices = years_choices)
    months_choices = [
        ("", "Months"),
        ("0", "Fresher"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("9+", "9+"),
    ]
    months = models.CharField(max_length = 2, null = True, choices = months_choices)
    job_choices = [
        ("", "Role"),
        ("UI/UX Designer", "UI/UX Designer"),
        ("Front-end Developer", "Front-end Developer"),
        ("Back-end Developer", "Back-end Developer"),
        ("Software Tester", "Software Tester"),
        ("Project Manager", "Project Manager"),
    ]
    job_role = models.CharField(max_length = 30, choices = job_choices)
    address_line_1 = models.CharField(max_length = 200, null = True)
    address_line_2 = models.CharField(max_length = 100, null = True)
    city = models.CharField(max_length = 30, null = True)
    state = models.CharField(max_length = 30, null = True)
    country = models.CharField(max_length = 30, null = True)
    zip_code = models.CharField(max_length = 7, null = True)

    def __str__(self):
        return self.full_name 