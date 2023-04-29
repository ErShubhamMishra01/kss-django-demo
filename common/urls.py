
from django.contrib import admin
from django.urls import path
import common.views as cviews
urlpatterns = [
    path('', cviews.index),
    path('aboutus/', cviews.aboutus),
    path('contactus/', cviews.contactus),
    path('register/', cviews.register),
    path('saveRegister/', cviews.saveRegister),


]
