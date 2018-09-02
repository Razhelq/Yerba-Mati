"""yerbamat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from yerba_mat.views import IndexView, CategoryView, CategoryAddView, ProductAddView, ProductDetailsView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^index/$', IndexView.as_view(), name='index'),
    url(r'^category_view/(?P<id>(\d)+)/$', CategoryView.as_view(), name='category-view'),
    url(r'^category_add/$', CategoryAddView.as_view(), name='category-add'),
    url(r'^product_add/$', ProductAddView.as_view(), name='product-add'),
    url(r'^product_details/(?P<id>(\d)+)/$', ProductDetailsView.as_view(), name='product-details')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)