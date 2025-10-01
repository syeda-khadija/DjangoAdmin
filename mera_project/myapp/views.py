from http.client import responses

import requests
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from mera_project.firebase_config import db

# Create your views here.

def register(req):
    if req.method == "POST":
        n = req.POST.get("name")
        e = req.POST.get("email")
        p = req.POST.get("password")


        if not n or not e or not p:
            messages.error(req, "All Fields are required")
            return redirect("reg")

        if len(p) < 8:
            messages.error(req, "Password must be 8 characters long")
            return redirect("reg")
        url =f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={settings.FIRE}"
        playload = {
            "email" : e,
            "password" : p,
            "returnSecureToken": True

        }

        response = requests.post(url, playload)

        if response.status_code == 200:
            errorMsg= response.json()
            db.collection("User").add({
                "Name" : n,
                "Email" : e,
                "Pswd" : p,
                "Role" : "User",

            })

            messages.success(req, "User Registered Successfully ✅ Now Login")
            return redirect("log")  # 👈 ab login page pe bhejega

        else:
            error_msg = response.json().get("error", {}).get("message", "Something went wrong")
            messages.error(req, f"Registration Failed: {error_msg}")
            return redirect("reg")

    return render(req, "myapp/registration.html")

def Login(req):
    if req.method == "POST":
        e = req.POST.get("email")
        p = req.POST.get("password")

        if not e or not p:
            messages.error(req, "All Fields are Required")
            return redirect("log")

        url =f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={settings.FIRE}"
        playload = {
            "email": e,
            "password": p,
            "returnSecureToken": True
        }
        res = requests.post(url, json=playload)

        if res.status_code == 200:
            userinfo = res.json()
            req.session["email"] = userinfo.get("email")
            return redirect("home")   # 👈 fixed here
        else:
            error = res.json().get("error", {}).get("message", "Message Not Found")
            print(error)
            if error == "INVALID_LOGIN_CREDIENTIALS":
                messages.error(req, "Invalid credentials, Login Again")
            elif error == "INVALID_PASSWORD":
                messages.error(req, "Password is Incorrect")
            return redirect("log")
    return render(req, "myapp/login.html")


def home(request):
    email = request.session.get("email")   # session se email nikalo
    return render(request, "myapp/home.html", {"email": email})



def contact(request):
    if request.method == "POST":
        n = request.POST.get("name")
        e = request.POST.get("email")
        s = request.POST.get("subject")
        m = request.POST.get("message")

        contact_data = {
            "name": n,
            "email": e,
            "subject": s,
            "message": m
        }
        db.collection("contacts").add(contact_data)

        messages.success(request, "Your message has been sent successfully!")
        return redirect("con")
    return render(request,"myapp/contact.html")


def service(request):
    return render(request,"myapp/service.html")

def service_details(request):
    return render(request,"myapp/service_details.html")

def blog_details(request):
    return render(request,"myapp/blog_details.html")

def pricing(request):
    return render(request,"myapp/pricing.html")

def blog(request):
    return render(request,"myapp/blog.html")