from django.shortcuts import render, HttpResponse


# Create your views here.
def admin(request):
    return HttpResponse("this is user admin")
