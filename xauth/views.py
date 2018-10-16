from django.shortcuts import render

# Create your views here.
from django.views import View


class Home(View):
    @classmethod
    def as_view(cls):
        return 'Hello world'
