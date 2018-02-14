from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve as static_serve

import session_csrf

from wagtail.wagtailadmin import urls as wagtailadmin_urls

from coss.base import views


session_csrf.monkeypatch()

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),

    # Wagtail admin page
    url(r'^cms-admin/', include(wagtailadmin_urls)),

    # contribute.json url
    url(r'^(?P<path>contribute\.json)$', static_serve,
        {'document_root': settings.STATIC_ROOT}),
]
