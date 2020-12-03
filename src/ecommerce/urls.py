from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView


from products.views import (
    ProductListView,
    product_list_view,
    ProductDetailView,
    ProductDetailSlugView,
    product_detail_view,
    ProductFeaturedDetailView,
    ProductFeaturedListView,
)


from .views import home_page, about_page, contact_page, login_page, register_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('contact/', contact_page, name='contact'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('bootstrap/', TemplateView.as_view(template_name='bootstrap/example.html')),
    # path('products/', include("products.urls")),
    path('searchs/', include("search.urls"), name='search'),
    path('featured/', ProductFeaturedListView.as_view()),
    path('featured/<int:pk>', ProductFeaturedDetailView.as_view()),
    path('products/', ProductListView.as_view(), name='products'),
    path('products/<int:pk>', ProductDetailView.as_view()),
    path('products/<slug:slug>/', ProductDetailSlugView.as_view(), name='detail'),
    path('products-fbv/<int:pk>', product_detail_view),
    path('products-fbv/', product_list_view),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
