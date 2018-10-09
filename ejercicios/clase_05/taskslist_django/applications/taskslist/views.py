from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.views import generic
# Create your views here.

from . import models


class List(generic.ListView):
    template_name = "list.html"
    queryset = models.Task.objects.all()
    context_object_name = "list"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(List, self).get_context_data(**kwargs)

        context['saludo'] = "Hola"

        return context


class Create(generic.CreateView):
    template_name = "create.html"
    model = models.Task
    fields = "__all__"
    success_url = "/"


    def form_valid(self, form):
        self.object = form.save()
        self.object.task = "Mi contenido"
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class Update(generic.UpdateView):
    template_name = "create.html"
    model = models.Task
    fields = "__all__"
    success_url = "/"

class Delete(generic.DeleteView):
    template_name = "delete.html"
    model = models.Task
    context_object_name = "task"
    success_url = "/"
