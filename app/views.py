from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):

    return render(request, 'add_confession.html')


def addConfession(request):

    rdata = request.POST
    print(f"rdata :: ", rdata)

    return HttpResponse("Added!")
    # return render(request, 'suc')


