from django.shortcuts import render, redirect
from .models import Pet
from django.contrib import messages
from django.views.generic import TemplateView
from django.db.models import Q

from pets.forms import PetForm
from pets.models import Pet


class HomeView(TemplateView):
    template_name = 'pets/home.html'

    def get(self, request):
        form = PetForm()
        query = request.GET.get('q')

        if query:
            results = Pet.objects.filter(
                Q(name__icontains=query) | Q(address__icontains=query) | Q(city__icontains=query))
        else:
            results = Pet.objects.all()

        args = {'form': form, 'pets': results}

        return render(request, self.template_name, args)


class AddPetsView(TemplateView):
    template_name = 'pets/addpets.html'

    def get(self, request):
        form = PetForm()
        pets = Pet.objects.all()
        args = {'form': form, 'pets': pets}
        return render(request, self.template_name, args)

    def post(self, request):
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = PetForm()
            return redirect('home')

        args = {'forms': form}
        return render(request, self.template_name, args)
