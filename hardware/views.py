from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Toch_dost, Region, Ustr
from django.views import generic
# Create your views here.

def toch_dost(request):
    return HttpResponse("Это страница узла связи, преславутая ip карта")

def detail(request):
    return HttpResponse("Это страница утройства")

def overview(request):

    return HttpResponse("Это страница с каналами и узлами")

class IndexView(generic.ListView):
    model = Region
    template_name = 'hardware/regions.html'
    context_object_name = 'all_regions'

    def get_queryset(self):
        
        return Region.objects.order_by('name')

class Toch_dost_View(generic.ListView):
    model = Toch_dost
    template_name = 'hardware/toch_dost.html'
    
    ''' def get_queryset(self):
       # self.equip = get_object_or_404(Toch_dost, name=self.args[0])
        return Toch_dost.objects.filter(region=self.region)

      '''

