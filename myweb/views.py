from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


class MyWeb:

    def index(self, r):
        return HttpResponse('ok')