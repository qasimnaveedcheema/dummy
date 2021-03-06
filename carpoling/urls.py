from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views
from django.views.generic import TemplateView

app_name= 'carpoling'

urlpatterns = [
    url(r'^$', login_required(views.HomeView.as_view()), name='home'),
    url(r'^success/$',TemplateView.as_view(template_name='carpoling/success.html'),name ="success"),
]