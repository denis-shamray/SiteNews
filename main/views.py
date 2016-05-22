from copy import copy
import datetime
import json
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import View
from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import resolve
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView


class BaseView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)

        return context


class IndexView(BaseView):
    template_name = "index.html"


class ContactView(BaseView):
    template_name = "contact.html"


class BlogView(BaseView):
    template_name = "index.html"


class ColumnsView(BaseView):
    template_name = "index.html"


class FullwidthView(BaseView):
    template_name = "index.html"


class PagewithsidebarView(BaseView):
    template_name = "index.html"


class PortfolioView(BaseView):
    template_name = "portfolio.html"


class Portfolio_postView(BaseView):
    template_name = "index.html"


class PostView(BaseView):
    template_name = "post.html"


class Tab_toggle_tableView(BaseView):
    template_name = "index.html"


class TestimonialsView(BaseView):
    template_name = "index.html"


class TypographyView(BaseView):
    template_name = "index.html"


class Button_boxes_imagesView(BaseView):
    template_name = "index.html"