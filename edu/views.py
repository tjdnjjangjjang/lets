from django.views.generic import View
from django.shortcuts import render

class Index(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)
