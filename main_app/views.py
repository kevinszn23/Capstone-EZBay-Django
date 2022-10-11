from django.shortcuts import render
from .models import Listing
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"
    
@method_decorator(login_required, name='dispatch')
class ListingsList(TemplateView):
    template_name = "listings_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["artists"] = Listing.objects.filter(name__icontains=name, user=self.request.user)
            context["header"] = f"Searching for {name}"
        else:
            context["listings"] = Listing.objects.filter(user=self.request.user)
            context["header"] = f"Searching for {name}"
        return context

class ListingsCreate(CreateView):
    model = Listing
    fields = ['name', 'img', 'ships_from', 'price', 'condition', 'shipping_details', 'delivery', 'returns', 'payments', 'authenticity', 'money_back', 'seller_information']
    template_name = "listings_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ListingsCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('listings_detail', kwargs={'pk': self.object.pk})

class ListingsDetail(DetailView):
    model = Listing
    template_name = "listings_detail.html"

class ListingsUpdate(UpdateView):
    model = Listing
    fields = ['name', 'img', 'ships_from', 'price', 'condition', 'shipping_details', 'delivery', 'returns', 'payments', 'authenticity', 'money_back', 'seller_information']
    template_name = "listings_update.html"
    def get_success_url(self):
        return reverse('listings_detail', kwargs={'pk': self.object.pk})

class ListingsDelete(DeleteView):
    model = Listing
    template_name = "listings_delete_confirmation.html"
    success_url = "/listings/"

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("artist_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
