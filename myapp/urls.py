from django.urls import path
from . import views

urlpatterns=[

    path('',views.home, name ='home'),
    path('my_search/',views.my_search, name = 'my_search'),
]