"""automatas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from afd import views as afd_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

urlpatterns.extend(
    [
        url(r'^automatas_finitos/$', afd_views.automatas),
        url(r'^afd/grafico/$', afd_views.grafico),
        url(r'^afnd/grafico_afnd/$', afd_views.grafico_afnd),
        url(r'^afnd/grafico_afndlamda/$', afd_views.grafico_afndlamda),
    ]
)