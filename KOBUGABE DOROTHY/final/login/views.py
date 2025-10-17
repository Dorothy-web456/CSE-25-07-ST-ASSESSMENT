from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import StaffAuthenticationForm, CustomUserForm


def register(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = CustomUserForm()
    context = {"form": form}
    return render(request, "registration.html", context)

def login_user(request):
    if request.method == "POST":
        form = StaffAuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("login.html")
    else:
        form = StaffAuthenticationForm()
    context = {"form": form}
    return render(request, "registration.html", context)