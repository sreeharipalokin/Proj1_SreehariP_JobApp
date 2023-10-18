// input from form
const form = document.getElementById('form')
const fullname = document.getElementById('fullname') 
const phone = document.getElementById('phone-number');
const email = document.getElementById('email');
const dob = document.getElementById('dob');
const role = document.getElementById('job-role');
const male = document.getElementById('male');
const female = document.getElementById('female');
const others = document.getElementById('others');

// error signals
const error_fname = document.getElementById('error-fname')
const error_phone = document.getElementById('error-phone')
const error_email = document.getElementById('error-email')
const error_dob = document.getElementById('error-dob')
const error_role = document.getElementById('error-role')
const error_gender = document.getElementById('error-gender')

// submit event
form.addEventListener('submit', (event) => {
    
   validateFullName(event);
   validatePhoneNumber(event);
   validateEmail(event);
   validateDob(event);
   validateJobRole(event);
//    validateGender(event);
   
});


// validate fullName

function validateFullName(event){
    let messages = []
    const fullNameRegex = /^[a-zA-Z ]+$/ 

    if (fullname.value === '' || fullname.value == null){
        messages.push('Name cannot be empty')
        window.scrollTo(0,0)
    } 
    else if (!fullNameRegex.test(fullname.value)) {
        messages.push('Error in full name')
        window.scrollTo(0,0)
    } 
    else if (fullname.value.length < 3){
        messages.push('Minimum 3 characters required')
        window.scrollTo(0,0)
    }
    else if (fullname.value.length > 75){
        messages.push('Maximum 75 characters allowed')
        window.scrollTo(0,0)
    }
    else {
        error_fname.innerText = messages.join(', ');
    }
    
    
    if (messages.length > 0) {
        event.preventDefault();
        error_fname.innerText = messages.join(', ');
    }    
}

form.addEventListener('change', (event) => {
    validateFullName(event);
  
});

// validate phoneNumber

function validatePhoneNumber(event) {
    let messages = []
    const phoneRegex = /^\d{10}$/

    if(phone.value === ''|| phone.value == null) {
        messages.push('Phone number cannot be empty')
        window.scrollTo(0,0)
    } 
    else if (!phoneRegex.test(phone.value)){
        messages.push('Invalid phone number')
        window.scrollTo(0,0)
    } 
    else {
        error_phone.innerText = messages.join(', ')   
    }
    
    if (messages.length > 0) {
        event.preventDefault();
        error_phone.innerText = messages.join(', ')
    }
}


form.addEventListener('change', (event) => {
    validatePhoneNumber(event);
});

// validate email

function validateEmail(event) {
    let messages = []
    const emailRegex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/

    if(email.value === '' || email.value == null) {
        messages.push('Email ID cannot be empty')
        window.scrollTo(0,0)
    }
    else if (!emailRegex.test(email.value)) {
        messages.push('Invalid Email ID')
        window.scrollTo(0,0)
    }
     else {
        error_email.innerText = messages.join(', ')
    }
    
    if (messages.length > 0) {
        event.preventDefault();
        error_email.innerText = messages.join(', ')
    }
}


form.addEventListener('change', (event) => {
    validateEmail(event);
});


// validate dob

function validateDob(event) {
    const currDate = new Date(); 
    const year = currDate.getFullYear();
    const month = String(currDate.getMonth() +1).padStart(2, '0');
    const day = String(currDate.getDate()).padStart(2, '0');
    const today = `${year}-${month}-${day}`;  // current date

    const givenDate = dob.value;      // the date from input 'date' field
    
    const date1 = new Date(today);
    const date2 = new Date(givenDate);
    const timeDiff = Math.floor((date1-date2)/(1000*60*60*24*365.25));
    let messages = []

    if (timeDiff < 18) {
        messages.push('Not eligible, the applicant should be minimum 18 years old ')
        window.scrollTo(0,0)
    } 
    else if (dob.value === '' || dob.value == null){
        messages.push('DOB cannot be empty')
        window.scrollTo(0,0)
    }
    else {
        error_dob.innerText = messages.join(', ')
    }
    if (messages.length > 0) {
        event.preventDefault();
        error_dob.innerText = messages.join(', ')
    }
}

form.addEventListener('change', (event) => {
    validateDob(event);
})

// validate Job Role

function validateJobRole(event){
   let messages = []
   if (role.value == "" || role.value == null){
    messages.push('Please select a role from the given options')
    window.scrollTo(0,0)
   }
   else {
    error_role.innerText = messages.join(', ')
   }
   if (messages.length > 0) {
    event.preventDefault();
    error_role.innerText = messages.join(', ')
    }
}

form.addEventListener('change', (event) => {
    validateJobRole(event);
})

// validate Gender

// function validateGender(event){
//     let messages = []
//     if(!male.value && !female.value && !others.value){
//         messages.push('Select a field')
//     }
//     else{
//         error_gender.innerText = messages.join(', ')  
//     }
//     if (messages.length > 0) {
//         event.preventDefault();
//         error_gender.innerText = messages.join(', ')
//     }
// }

// form.addEventListener('change', (event) => {
//     validateGender(event);
// })

function preventbackbutton(){window.history.forward();}
setTimeout("preventbackbutton()", 0);
window.onunload=function(){null};
