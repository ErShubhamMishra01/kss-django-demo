
from django.contrib import admin
from django.urls import path, include
import common.views as cviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cviews.index),

    path('common/', include('common.urls')),
    
]
