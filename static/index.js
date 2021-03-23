function validate_dob(date, flag) {
    var arr = date.split('-');
    if (arr[0] <= 1998 || arr[0] >= 2005)
        alert("dob should be in range(1998,2005)");
    else {
        flag += 1;
    }
    return flag;
}

function validate_age(age, flag) {
    if (age >= 12 && age <= 23) {
        flag += 1;
    } else {
        alert("age should be in range(12,23).")
    }
    return flag;
}
var number = 0;

function validate_pass(pass, pass1, flag) {
    if (pass != pass1) {
        alert("password and confirm password field should be same.")
    } else if (pass.length < 8) {
        alert("password length should be atleast 8 ")
    } else if (pass.length > 20) {
        alert("max length of password should be 20.")
    } else {
        flag += 2
    }
    return flag;
}

function sendEmail(mail) {
    number = Math.floor(Math.random() * (999999 - 100000 + 1)) + 100000;
    var name = document.getElementById("name").value;
    if (name == '') {
        name = "There";
    }
    Email.send({
        SecureToken: "fbf31702-bb7f-4a4e-9c1c-4ccf17ee777f",
        To: mail,
        From: "no.reply.python.py@gmail.com",
        Subject: "Your OTP For One Time Crediantials by NestedForms.com",
        Body: "Hello " + name + ". Your One Time Password For Login is " + number + " is valid for 6 minutes. Please Don't Refresh Your Browser Window.",
    }).then(function(response) {
        if (response == 'OK')
            alert("OTP send to " + mail)
        else {
            alert(response);
        }
    });
    return number;
}

function handler() {
    var mail = document.getElementById("mail").value;
    number = sendEmail(mail);
}


function validate() {
    var pass = document.getElementById("pass").value;
    var pass1 = document.getElementById("pass1").value;
    var age = document.getElementById("age").value;
    var mail = document.getElementById("mail").value;
    var dob = document.getElementById("dob").value;
    var otp = document.getElementById("otp").value;
    flag = 0
    flag = validate_dob(dob, flag);
    flag = validate_age(age, flag);
    flag = validate_pass(pass, pass1, flag);
    if (number == otp && flag == 4) {
        alert("Data Verified Press Ok to Begin..");
        return true;
    } else {
        alert("Please Fill Data Correctly.");
        return false;
    }
}