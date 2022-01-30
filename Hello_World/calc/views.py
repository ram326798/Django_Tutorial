from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    # In order to show output with out templates
    # return HttpResponse("Hello world")
    # in order to show outpput using template
    # name is a variable that is taking data to home.html
    return render(request, 'home.html', {'name': 'Ram'})


def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1+val2

    return render(request, 'result.html', {'result': res})
