from django.shortcuts import render, HttpResponse , redirect

import api

# Create your views here.

def redirect_index(request):
    return redirect("home", days_range=30,currencies="USD")

def dashboard(request,days_range,currencies):

    days,rates = api.get_rates(currencies=currencies.split(","),days=days_range)
    page_label = {7:"Last week",30:"Last Mounth",365:"Last Year"}.get(days_range,"Personalize")

    return render(request,"devise/index.html",context={"data":rates,
                                                       "days_labels":days,
                                                       "currencies":currencies,
                                                       "page_label":page_label})
