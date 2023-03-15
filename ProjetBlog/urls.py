"""ProjetBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from ProjetBlog import settings
from blog.views import home, detail_article, modifier_comment, supprimer_comment, about, article_par_categ

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('', home, name='home'),
    path('details/<str:slug>', detail_article, name='detail_article'),
    path('modifier-commentaire/<int:id>', modifier_comment, name='modifier_comment'),
    path('supprimer_commentaire/<int:id>/', supprimer_comment, name='supprimer_comment'),
    path('blog/apropos/', about, name='about'),
    path('articles/<str:slug>/', article_par_categ, name='article_par_categ'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
