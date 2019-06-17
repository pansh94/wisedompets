from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Pets, Reason


def home(request):
    pets_info = Pets.objects.all()
    return render(request,"home.html",{"pets_info" : pets_info})


def pet_detail(request, id):
    context = {}
    try:
        pet_info = Pets.objects.get(id=id)
        vacc = Reason.objects.filter(pets=pet_info)
        context = {
                    "pet_info":pet_info,
                    "vaccine":vacc,
                   }
        print(vacc.count())
    except Pets.DoesNotExist or Reason.DoesNotExist:
        raise Http404("Pet is not present.")

    return render(request, "pet_detail.html", context)
