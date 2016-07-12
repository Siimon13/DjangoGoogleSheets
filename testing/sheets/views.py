from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import loader
from django.core.urlresolvers import reverse
import codes
import os.path

# Create your views here.
def index(request):
    #data = quickstart.display_Sheets()
    data = codes.display_Sheets()
    if data == "No data found." :
        return HttpResponseNotFound('<h1>Data Not Found</h1>')
    else:
        #return HttpResponse(data)
        return render(request, 'index.html', {'data' : data})
