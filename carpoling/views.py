from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import CreateView
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth import logout
from models import Registration
		
class IndexView(generic.TemplateView):
    template_name = 'carpoling/index2.html'
    context_object_name = 'latest_question_list'

    
class HomeView(CreateView):
    template_name = 'carpoling/home.html'
    model = Registration
    fields = ['first_name','last_name','email','phone','date','time']
    success_url = '/carpoling/success/'
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')