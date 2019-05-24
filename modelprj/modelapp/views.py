from django.shortcuts import render
from .models import Twice

def twice(request):
    members = Twice.objects.filter(nationality = '일본')
    return render(request, "home.html", {'japanese' : members})