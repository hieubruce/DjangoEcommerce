from django.urls import path, re_path

from .views import (
        cart_home,
        cart_update,
        checkout_home,
        )

urlpatterns = [
    path('', cart_home, name='home'),
    re_path(r'^checkout/$', checkout_home, name='checkout'),
    re_path(r'^update/$', cart_update, name='update'),
]