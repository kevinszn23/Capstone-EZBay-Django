from pipes import Template
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
import os
import datetime
import sys
import requests
from ebaysdk.finding import Connection
from ebaysdk.exception import ConnectionError

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
            context["listings"] = Listing.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["listings"] = Listing.objects.all()
            context["header"] = f"Searching for {name}"
        return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     name = self.request.GET.get("name")
    #     if name == None:
    #         context["header"] = f"Searching for {name}"
    #     else:
    #         print(name)
    #         e = ebay_search_api(API_KEY, name)
    #         context["api"] = e.fetch()
    #         e.parse()
    #         print(context["api"])
    #     return context
    
# def itemId(request):
#     response=requests.get("https://api.ebay.com/buy/browse/v1/item/{item.id}").json()
#     return render(request,"listings_itemId.html",{"response": response})

# from dotenv import load_dotenv
# load_dotenv()
# API_KEY=os.getenv("api_key")

# class ebay_search_api(object):
#     def __init__(self, API_KEY, st):
#         self.api_key = API_KEY
#         self.st = st

#     def fetch(self):
#         try:
#             api = Connection(appid=self.api_key, config_file=None, siteid="EBAY-US")
#             response = api.execute('findItemsAdvanced', {'keywords': self.st})
            # print(response.reply)
            # print(f"Total items: {response.reply.paginationOutput.totalEntries}\n")

            # for item in response.reply.searchResult.item:
            #     print(f"Title: {item.title}, Price: {item.sellingStatus.currentPrice.value}")
            #     # print(f"Condition: {item.condition.conditionDisplayName}")
            #     print(f"Buy it now: {item.listingInfo.buyItNowAvailable}")
            #     print(f"Country: {item.country}")
            #     print(f"End time: {item.listingInfo.endTime}")
            #     print(f"URL: {item.viewItemURL}")
            #     try:
            #         print(f"Watchers: {item.listingInfo.watchCount}\n")
            #     except:
            #         pass

    #         return response.reply.searchResult.item

    #     except ConnectionError as e:
    #         print(e)
    #         print(e.response.dict())

    # def parse(self):
    #     pass

# if __name__ == "__main__":
#     st = sys.argv[1]
#     e = ebay_api(API_KEY, st)
#     e.fetch()
#     e.parse()


# class ListingsItemId(TemplateView):
#     template_name = "listings_itemId.html"


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
            return redirect("listings_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

def shows_slides(request):
    return render(request, "home.html")