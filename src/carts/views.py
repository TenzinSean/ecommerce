from django.shortcuts import render

# Create your views here.


def cart_home(request):
    #key = request.session.session_key
    # print(key)
    request.session["cart_id"] = 12
    request.session["user"] = request.user.username
    return render(request, "carts/home.html", {})
