from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db import models
from cars.models import Car
from cars.forms import CarModelForm

class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().filter(active=True).order_by('model')
        search = self.request.GET.get('q')
        if search:
            cars = cars.filter(
                models.Q(model__icontains=search) | 
                models.Q(brand__name__icontains=search)
            )
        return cars

class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars'

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
    context_object_name = 'car'

class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'
    
    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk':self.object.pk})

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars'

    def post(self, request, pk):
        car = Car.objects.get(pk=pk)
        car.active = False
        car.save()
        return redirect('cars_list')