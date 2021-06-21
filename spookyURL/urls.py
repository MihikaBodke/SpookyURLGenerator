"""spookyURL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from urlGenerator import views
admin.autodiscover()
from django.views.generic import TemplateView
from django.conf.urls import  url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about_us', TemplateView.as_view(template_name="about_us.html"), name='about_us'),
    path('contact_us', TemplateView.as_view(template_name="contact_us.html"), name='contact_us'),
    path('article/', TemplateView.as_view(template_name="article.html"), name='article'),
    path('<str:url>/', views.goToURL, name="" ),

    path('', views.index, name="index" ),

    path('', views.index, name="home" ),
]
# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)