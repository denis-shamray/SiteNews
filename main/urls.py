"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from main.views import IndexView
from main.views import ContactView
from main.views import BlogView
from main.views import ColumnsView
from main.views import FullwidthView
from main.views import PagewithsidebarView
from main.views import PortfolioView
from main.views import Portfolio_postView
from main.views import PostView
from main.views import Tab_toggle_tableView
from main.views import TestimonialsView
from main.views import TypographyView
from main.views import Button_boxes_imagesView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^contact$', ContactView.as_view(), name='contact'),
    url(r'^blog$', BlogView.as_view(), name='blog'),
    url(r'^columns$', ColumnsView.as_view(), name='columns'),
    url(r'^fullwidth$', FullwidthView.as_view(), name='fullwidth'),
    url(r'^pagewithsidebar$', PagewithsidebarView.as_view(), name='pagewithsidebar'),
    url(r'^portfolio$', PortfolioView.as_view(), name='portfolio'),
    url(r'^portfolio-post$', Portfolio_postView.as_view(), name='portfolio-post'),
    url(r'^post$', PostView.as_view(), name='post'),
    url(r'^tab-toggle-table$', Tab_toggle_tableView.as_view(), name='tab-toggle-table'),
    url(r'^testimonials$', TestimonialsView.as_view(), name='testimonials'),
    url(r'^typography$', TypographyView.as_view(), name='typography'),
    url(r'^button-boxes-images$', Button_boxes_imagesView.as_view(), name='button-boxes-images'),


    url(r'^files/', include('db_file_storage.urls')),
]
