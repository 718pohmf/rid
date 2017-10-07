from django.shortcuts import render
from addresources.models import addresources, addmatchingresources, editresources, Technologies


def index(request):
    return render(request, 'webapp/home.html') # this two parameters are compulsory

def database(request):
    all_resources=addresources.objects.all()
    return render(request, 'webapp/database.html', {'all_resources':all_resources})

def filter(request):
    all_resources=addresources.objects.all()
    return render(request, 'webapp/filter.html', {'all_resources':all_resources})

def calculator(request):
    all_resources=addresources.objects.all()
    return render(request, 'webapp/calculator.html', {'all_resources':all_resources})

def homepage(request):
    return render(request, 'webapp/homepage.html')

def filtervisitor(request):
    all_resources=addresources.objects.all()
    return render(request, 'webapp/filtervisitor.html', {'all_resources':all_resources})

def contact(request):
    return render(request, 'webapp/contactus.html')
