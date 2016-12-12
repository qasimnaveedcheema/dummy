
from django.conf.urls import include, url
from django.contrib import admin
from carpoling import views
from django.contrib.auth .views import login
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='home'),
    url(r'^logout/$',views.logout_view, name='logout'),
    url(r'^poll/', include('poll.urls')),
    url(r'^carpoling/', include('carpoling.urls')),
    url(r'^login/$',login, {'template_name': 'carpoling/login.html'},name = 'django.contrib.auth.views.login'),
    url(r'^admin/', admin.site.urls),
]