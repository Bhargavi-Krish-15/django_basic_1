from django.shortcuts import render
from datetime import date


# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, this is the index view!") #or return render(request, 'your_template.html')


def get_date(request):
    today = date.today()
    template = "<html>" \
                "Today's date is {}" \
               "</html>".format(today)
    return HttpResponse(content=template)