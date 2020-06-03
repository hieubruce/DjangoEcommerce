
from django.urls import path, re_path

from products.views import (
        ProductListView,
        ProductDetailSlugView,
        list_of_product_by_category
        )



urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    re_path(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
    re_path(r'^category/(?P<category_slug>[\w-]+)/$', list_of_product_by_category, name='list_of_product_by_category'),
]
