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


class IndexView(BaseView):
    template_name = "index.html"
