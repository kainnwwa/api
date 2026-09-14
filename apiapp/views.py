from django.shortcuts import View
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Product 


class MyView(View):
    def get(self, request):
        

