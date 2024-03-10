from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

# Create your views here.

months = {
    'january':'EAT NO MEAT',
    'feburary':'No Shave',
    'march':'Lets Smoke',
    'april':'ok',
    'may':'But, i will smoke good ',
    'june':'Quality of',
    'july':'WEED',
    'august':'Awesome',
    'september':'Chilling',
    'october':'Gandhi ji',
    'november':'phookte h Kya?',
    'december': None
}

def all_months(request):
    month = list(months.keys())
    return render(request,"months/index.html",
                  {
                      "months":month
                  })

def indiviual_month_by_num(request, month):
    month_num = list(months.keys())
    if month > len(months) or month < 1 :
        return HttpResponseNotFound("Month doesn't exists")
    number = month_num[month-1]
    redirect_to_indi = reverse("Indiviual month", args=[number])
    return HttpResponseRedirect(redirect_to_indi)


def indiviual_month(request, month):
    try:
        list_of_mvalue = months[month] 
        return render(request,"months/IndiviualM.html", {
            "month_name": month,
            "month_value": list_of_mvalue
        })
    except:
        raise Http404()

