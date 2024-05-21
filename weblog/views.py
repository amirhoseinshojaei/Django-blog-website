from django.shortcuts import render
from django.views.decorators.http import require_http_methods
# Create your views here.

require_http_methods(["GET"])
def index(request):

    context={}

    return render(request,'blog/home.html',context)