from django.contrib import admin
from .models import ApplicantDetails,ApplicantDetailsModel
# Register your models here.

admin.site.register(ApplicantDetails)

class ApplicantsDisplay(admin.ModelAdmin):
    list_display = ("full_name", "country_code", "phone_number", "email_id", "job_role")

admin.site.register(ApplicantDetailsModel, ApplicantsDisplay)
