from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import openpyxl


@login_required
def index(request):
    return render(request, 'bases/index.html', locals())



