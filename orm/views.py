from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpRequest
from django.views.generic import DeleteView
from .models import Human
# Create your views here.


class List(TemplateView):
    template_name = 'base.html'

    def get(self, request):
        all_humans = Human.objects.all()
        ctx = {
            'all_humans': all_humans,
        }
        return render(request, self.template_name, ctx)


class HumanDelete(DeleteView):
    model = Human
    success_url = '/'
    template_name = 'human_delete.html'
