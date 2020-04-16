
from django.urls import path, re_path

from products.views import (
        ProductListView,
        # product_list_view,
        # ProductDetailView,
        ProductDetailSlugView,
        # product_detail_view,
        # ProductFeaturedListView,
        # ProductFeaturedDetailView
        )



urlpatterns = [
    path('', ProductListView.as_view()),
    re_path(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
]
