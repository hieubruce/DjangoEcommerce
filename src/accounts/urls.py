from django.urls import path, re_path

from .views import (
        AccountHomeView,
        UserDetailUpdateView,
        )

urlpatterns = [
    path('', AccountHomeView.as_view(), name='home'),
    path('details/', UserDetailUpdateView.as_view(), name='user-update'),
]
