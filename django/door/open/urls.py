from django.contrib import admin
from django.urls import path
from open import views

urlpatterns =[
   path('',views.home,name="home"),
   path('contact/',views.contact,name="contact"),
   path('history.html/',views.history,name="history")
]