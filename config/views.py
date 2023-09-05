from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
import random
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# def main(request):
#     return HttpResponse("안뇽~")
#
#
# def burger_list(request):
#     return HttpResponse("안뇽~~~~~~~~~~~~~~~~~~~~~~")

def main(request):
    return render(request, "main.html")


def burger_list(request):
    return render(request, "burger_list.html")


def index(request):
    return render(request, "index.html")