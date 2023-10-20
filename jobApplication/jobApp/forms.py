from django.forms import ModelForm, TextInput, EmailInput, Select, widgets, RadioSelect
from .models import ApplicantDetailsModel

class ApplicationForm(ModelForm):
    class Meta:
        model = ApplicantDetailsModel
        fields = '__all__'
        labels = {
            "full_name": "Full Name",
            "phone_number": "Contact",
            "email_id": "Email ID",
            "dob": "Date Of Birth",
            "gender": "Gender",
            "years": "Experience",
            "job_role": "Preferred Role",
            "address_line_1": "Address",
        }

        widgets = {
                 "full_name": TextInput(attrs={
                    "class": "full_name",
                    "placeholder": "Enter your full name"
                 }),

                 "country_code": Select(attrs = {
                    "class": "country_code",
                 }),

                 "phone_number": TextInput(attrs = {
                    "class": "phone_number",
                    "placeholder": "Enter your contact number",
                 }),

                 "email_id": EmailInput(attrs = {
                    "class": "email_id",
                    "placeholder": "Enter your Email ID"   
                 }),

                 "dob": widgets.DateInput(attrs = {
                    "type": "date",
                 }),

                 "gender": RadioSelect(attrs = {
                    "class": "gender"
                 }),

                 "years": Select(attrs = {
                    "class": "years"                  
                 }),

                 "months": Select(attrs = {
                    "class": "months"
                 }),

                 "job_role": Select(attrs = {
                    "class": "job_role"
                 }),

                "address_line_1": TextInput(attrs={
                    "class": "address_fields",
                    "placeholder": "Address Line 1"
                 }),

                 "address_line_2": TextInput(attrs={
                    "class": "address_fields",
                    "placeholder": "Address Line 2"
                 }),

                 "city": TextInput(attrs={
                    "class": "address_fields",
                    "placeholder": "District"
                 }),

                 "state": TextInput(attrs={
                    "class": "address_fields",
                    "placeholder": "State"
                 }),

                 "country": TextInput(attrs={
                    "class": "address_fields",
                    "placeholder": "Country"
                 }),

                 "zip_code": TextInput(attrs={
                    "class": "address_fields",
                    "placeholder": "Zip code"
                 })                
        }
