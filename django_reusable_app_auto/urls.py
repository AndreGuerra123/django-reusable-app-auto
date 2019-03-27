# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

app_name = 'django_reusable_app_auto'
urlpatterns = [
    url(r'', TemplateView.as_view(template_name='base.html')),
]
