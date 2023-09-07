from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import openpyxl


@login_required
def index(request):
    return redirect('wo_search')



