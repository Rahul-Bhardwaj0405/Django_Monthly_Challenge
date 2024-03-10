from django import views
from django.urls import path
from .import views

urlpatterns = [
    path("",views.all_months, name="index"),
    path("<int:month>", views.indiviual_month_by_num),
    path("<str:month>", views.indiviual_month, name="Indiviual month")
]
