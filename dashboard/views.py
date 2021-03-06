from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Reparaciones
from core.models import Slider

from django.urls import reverse_lazy


##################################################################################################
class Login(LoginView):
    template_name = "dashboard/login.html"
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('home')

##################################### CRUD REPARACIONES ############################################
class DashBoardList(LoginRequiredMixin, ListView):
    model = Reparaciones
    context_object_name = "reparaciones"
    template_name = "dashboard/CRUD-Reparaciones/reparaciones_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = context['reparaciones'].filter(Completa=False).count()
        return context

class DashBoardDetail(LoginRequiredMixin, DetailView):
    model = Reparaciones
    context_object_name = "reparacion"
    template_name = "dashboard/CRUD-Reparaciones/reparacion.html"


class DashBoardCreate(LoginRequiredMixin, CreateView):
    model = Reparaciones
    fields = "__all__"
    success_url = reverse_lazy('home')
    template_name = "dashboard/CRUD-Reparaciones/reparaciones_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DashBoardCreate, self).form_valid(form)

class DashBoardUpdate(LoginRequiredMixin, UpdateView):
    model = Reparaciones
    fields = "__all__"
    success_url = reverse_lazy("home")
    template_name = "dashboard/CRUD-Reparaciones/reparaciones_form.html"

class DashBoardDelete(LoginRequiredMixin, DeleteView):
    model = Reparaciones
    context_object_name = "reparacion"
    success_url = reverse_lazy('home')
    template_name = "dashboard/CRUD-Reparaciones/reparaciones_confirm_delete.html"




##################################### CRUD SLIDER ############################################
class SliderList(LoginRequiredMixin, ListView):
    model = Slider
    context_object_name = "sliders"
    template_name = "dashboard/CRUD-Slider/slider_list.html"

class SliderDetail(LoginRequiredMixin, DetailView):
    model = Slider
    context_object_name = "slider"
    template_name = "dashboard/CRUD-Slider/slider.html"

class SliderCreate(LoginRequiredMixin, CreateView):
    model = Slider
    fields = "__all__"
    success_url = reverse_lazy('Sliders')
    template_name = "dashboard/CRUD-Slider/slider_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SliderCreate, self).form_valid(form)

class SliderUpdate(LoginRequiredMixin, UpdateView):
    model = Slider
    fields = "__all__"
    success_url = reverse_lazy("home")
    template_name = "dashboard/CRUD-Slider/slider_form.html"

class SliderDelete(LoginRequiredMixin, DeleteView):
    model = Slider
    context_object_name = "slider"
    success_url = reverse_lazy('Sliders')
    template_name = "dashboard/CRUD-Slider/slider_confirm_delete.html"

