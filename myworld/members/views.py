from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members

# Create your views here.
def index(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mymembers': mymembers
    }
    return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['name']
  y = request.POST['modul']
  z = request.POST['gruppe']
  member = Members(name=x, modul=y, gruppe=z)
  member.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  member = Members.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  mymember = Members.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  name = request.POST['name']
  modul = request.POST['modul']
  gruppe = request.POST['gruppe']
  member = Members.objects.get(id=id)
  member.name = name
  member.modul = modul
  member.gruppe = gruppe
  member.save()
  return HttpResponseRedirect(reverse('index'))


#fra: https://www.w3schools.com/django/django_update_record.php