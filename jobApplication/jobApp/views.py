from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ApplicantDetails
from django.contrib import messages
from datetime import datetime, date
import re

# Create your views here.

def index(request):
    values = ApplicantDetails.objects.all().order_by('-id')
    return render(request, "jobapp/HomePage.html", {"values":values})

def add_user(request):
    if request.method == "POST":
        fname = request.POST['fullname']
        country_code = request.POST['country-code']
        phone = request.POST['phone-inp']
        email = request.POST['email']
        dob = request.POST['dob']
        gender = request.POST['gender']
        experience_years = request.POST['experience-years']
        experience_months = request.POST['experience-months']
        job_role = request.POST['job-role']
        address_line1 = request.POST['address-line-1']
        address_line2 = request.POST['address-line-2']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        zip_code = request.POST['zipcode']

        if (validateName(fname) and
            validateCode(country_code) and
            validateNumber(phone) and 
            validateEmail(email) and 
            validateDob(dob) and
            validateRole(job_role)
            ):
            details = ApplicantDetails.objects.create(
                full_name = fname,
                country_code = country_code,
                phone_number = phone,
                email_id = email,
                dob = dob,
                gender = gender,
                years = experience_years,
                months = experience_months,
                job_role = job_role,
                address_line_1 = address_line1,
                address_line_2 = address_line2,
                city = city,
                state = state,
                country = country,
                zip_code = zip_code
                )
            details.save()
            
            # messages.info(request,"Applicant successfuly registered")
            return redirect('index')
    return render(request, "jobapp/AppForm.html")

def validateName(fullname):
    if (fullname == "" or fullname == None or len(fullname) > 75 or len(fullname) < 3):
        return False
    else:
        return True  
    
def validateNumber(number):
    phonepattern = r'^\d{10}$'
    matchs = re.match(phonepattern, number)
    if((number == "") or (matchs is None)):
        return False
    else:
        return True

def validateEmail(email):
    emailpattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    matchs = re.match(emailpattern, email)
    if(( email== "") or (matchs is None)):
        return False
    else:
        return True  
 
def validateCode(code):
    if (code == "" or code == None or len(code) > 3):
        return False
    else:
        return True

def validateDob(dob):
    today = str(date.today())
    date1 = datetime.strptime(today, "%Y-%m-%d")
    date2 = datetime.strptime(dob, "%Y-%m-%d")
    time_diff = (date1 - date2).days
    if (dob == "" or dob == None or time_diff < 18):
        return False
    else:
        return True

def validateGender(gender):
    if (gender == "" or gender == None or len(gender) > 6):
        return False
    else:
        return True

def validateYears(years):
    if (years == "" or years == None):
        return False
    else:
        return True

def validateMonths(months):
    if (months == "" or months == None):
        return False
    else:
        return True

def validateRole(jobrole):
    if (jobrole == "" or jobrole == None):
        return False
    else:
        return True

def validateAddress(address):
    if (address == "" or address == None or len(address) > 200):
        return False
    else:
        return True

def validateCity(city):
    if (city == "" or city == None or len(city) > 30):
        return False
    else:
        return True

def validateState(state):
    if (state == "" or state == None or len(state) > 30):
        return False
    else:
        return True

def validateCountry(country):
    if (country == "" or country == None or len(country) > 30):
        return False
    else:
        return True

def validateZipcode(zipcode):
    if (zipcode == "" or zipcode == None or len(zipcode) > 6 or len(zipcode) < 6):
        return False
    else:
        return True
    

def edit_user(request, applicant_id):
    details = ApplicantDetails.objects.filter(id=applicant_id)
    if request.method == "POST":
        fname = request.POST['fullname']
        country_code = request.POST['country-code']
        phone = request.POST['phone-inp']
        email = request.POST['email']
        dob = request.POST['dob']
        gender = request.POST['gender']
        experience_years = request.POST['experience-years']
        experience_months = request.POST['experience-months']
        job_role = request.POST['job-role']
        address_line1 = request.POST['address-line-1']
        address_line2 = request.POST['address-line-2']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        zip_code = request.POST['zipcode']
        new_data = ApplicantDetails.objects.get(id=applicant_id)
          
        if (validateName(fname) and 
            validateCode(country_code) and
            validateNumber(phone) and 
            validateEmail(email) and 
            validateDob(dob) and
            validateRole(job_role)
            ):
            new_data.full_name = fname
            new_data.country_code = country_code
            new_data.phone_number = phone
            new_data.email_id = email
            new_data.dob = dob
            new_data.gender = gender
            new_data.years = experience_years
            new_data.months = experience_months
            new_data.job_role = job_role
            new_data.address_line_1 = address_line1
            new_data.address_line_2 = address_line2
            new_data.city = city
            new_data.state = state
            new_data.country = country
            new_data.zip_code = zip_code
            new_data.save()
            return redirect('index') 
    return render(request, "jobapp/Edit_page.html", {"details":details})

def del_user(request, applicant_id):
    ApplicantDetails.objects.get(id=applicant_id).delete()
    return redirect('index')