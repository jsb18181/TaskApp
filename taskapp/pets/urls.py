from django.conf.urls import url, include
from django.views.generic import TemplateView
from pets.views import HomeView, AddPetsView

from .models import Pet

urlpatterns = [

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^home/', HomeView.as_view(), name='home'),
    url(r'^home/results/', HomeView.as_view(), name='search'),
    url(r'^addpets/', AddPetsView.as_view(), name='addpets')
]
