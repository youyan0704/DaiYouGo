from django.shortcuts import render

# Create your views here.
from django.views import View


class Home(View):
    template_name = "xauth/login_origin.html"
    # template_name = "base.html"

    def get(self, request, *args, **kwargs):
        # form = self.form_class()
        return render(request, self.template_name)
