from django.conf.urls import url
from django.urls import path


from products.views import (
    ProductListView,
    # product_list_view,
    # ProductDetailView,
    ProductDetailSlugView,
    # product_detail_view,
    # ProductFeaturedDetailView,
    # ProductFeaturedListView,
)

urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('products/<slug:slug>', ProductDetailSlugView.as_view()),
]
