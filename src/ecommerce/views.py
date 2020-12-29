from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import get_user_model


from .forms import ContactForm, LoginForm, RegisterForm


def home_page(request):
    if not request.user.is_authenticated:
        return Login
    print(request.session.get("first_name", "Unknown"))
    # request.session["first_name"]
    context = {
        "title": "Hello World",
        "content": "Welcome to the homepage.",
    }

    if request.user.is_authenticated:
        context["premuim_content"] = "YEAHHH"
    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        "title": "About Page",
        "content": "Welcome to the aboutpage"
    }
    return render(request, "home_page.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact page",
        "content": "Welcome to the contactpage",
        "form": contact_form,
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == "POST":
    #     print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, "contact/view.html", context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print("User loggin in: ")
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            context['form'] = LoginForm()
            return redirect("/login")
        else:
            # Return an 'invalid login' error message.
            print("Error")
    return render(request, "auth/login.html", context)


User = get_user_model()


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, "auth/register.html", context)
