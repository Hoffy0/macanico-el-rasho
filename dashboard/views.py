from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Reparaciones

from django.urls import reverse_lazy


##################################################################################
class Login(LoginView):
    template_name = "dashboard/login.html"
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('home')

class DashBoardList(LoginRequiredMixin, ListView):
    model = Reparaciones
    context_object_name = "reparaciones"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = context['reparaciones'].filter(Completa=False).count()
        return context

class DashBoardDetail(LoginRequiredMixin, DetailView):
    model = Reparaciones
    context_object_name = "reparacion"
    template_name = "dashboard/reparacion.html"

class DashBoardCreate(LoginRequiredMixin, CreateView):
    model = Reparaciones
    fields = "__all__"
    success_url = reverse_lazy('home')
    template_name = "dashboard/reparaciones_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DashBoardCreate, self).form_valid(form)

class DashBoardUpdate(LoginRequiredMixin, UpdateView):
    model = Reparaciones
    fields = "__all__"
    success_url = reverse_lazy("home")

class DashBoardDelete(LoginRequiredMixin, DeleteView):
    model = Reparaciones
    context_object_name = "reparacion"
    success_url = reverse_lazy('home')
