from django.shortcuts import render
from .models import *

# Create your views here.
def test(request):
    return render(request, "testapp/test.html", {'rubrics': Rubric.objects.all()})

def get_rubric(request):
    pass