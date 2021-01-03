from django.shortcuts import render,redirect
from .models import Permit
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import PermitForm
from django.contrib import  messages


class IndexView(generic.ListView):
    template_name = "index.html"
    context_object_name = "permits"

    def get_queryset(self):
        """return all the added permits"""
        return Permit.objects.order_by('-creation_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



class  PermitCreate(CreateView):
    template_name = "create.html"
    form_class = PermitForm
    success_url = reverse_lazy('dig_permit:index')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)


    
    def form_invalid(self, form,**kwargs):
        #attempt dirty hack
        """try to get the capturepoint from form first
        if not clean get the data from the message"""
        print(form.errors)
        context = super().get_context_data(**kwargs)
        context["form"] = form


        for  k,v  in form.errors.items():
            messages.add_message(self.request, messages.ERROR, k)

        return redirect(reverse_lazy('dig_permit:create'))




class DetailView(generic.DetailView):
    model = Permit
    context_object_name = "permit"

    template_name =  "detail_view.html"



