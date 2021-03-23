from django.shortcuts import render
from email.message import EmailMessage
import smtplib
# Create your views here.
import pandas as pd

def home(request):
    return render(request,'index.html')

def mailer(to):
    sender_mail = "no.reply.python.py@gmail.com"   
    password_sender = "qwerty@123"

    message = EmailMessage()
    message['To'] = to
    message['From'] = sender_mail
    message['Subject'] = "Welcome User. to NestedForms.com"
    message.set_content("Hello User This is just a Confirmational mail that you have currently signed in to NestedForms.com")
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_mail, password_sender)
        server.send_message(message)
    except:
        pass

def store(request):
    
    df = pd.read_csv("data.csv")

    name = request.POST["name"]
    entry = request.POST["entry"]
    mail = request.POST["mail"]
    uname = request.POST["uname"]
    passwd = request.POST["pass"]
    age = request.POST["age"]
    dob = request.POST["dob"]

    for mails in df.Mail_id:
        if mail == mails:
            return render(request, 'result.html' ,{"result":"Error....Mail I'D Already Registered.:-/ "})

    for u_name in df.Username:
        if u_name == uname:
            return render(request, 'result.html' ,{"result":"Error....Username Not Available:-/ "})

    for entries in df.Entry_no:
        if entries == entry:
            return render(request, 'result.html' ,{"result":"Error....Entry Number Should be Unique:-/ "})

    df.loc[len(df.index)] = [name, entry, mail, uname,passwd,age,dob]

    df.to_csv("data.csv",index=False)

    return render(request, 'result.html' ,{"result":f"Success your token is {len(df.index)}"})

def signin(request):

    return render(request,'login.html')

def auth_login(request):
    df = pd.read_csv("data.csv")
    user = request.POST["name"]
    passwd = request.POST["pass"]
    fstr = f"Username=='{user}' & Password=='{passwd}'"
    output = df.query(fstr)
    if len(output) == 1:
        for mail in output.Mail_id:
            mailer(mail)
            return render(request, 'result.html' , {"result":"Successfully logged in."})
    else:
        temp = f"Username=='{user}'"
        output = df.query(temp)
        if len(output):
            return render(request, 'result.html' , {"result":"Wrong Password Make Sure You Remember it..."})
        else:
            return render(request, 'result.html' , {"result":"Can't find User You Requested For..."})