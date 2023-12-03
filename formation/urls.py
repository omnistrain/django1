"""
URL configuration for formation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from stock import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('groupes/', views.groupe_list, name='groupe-list'),
    path('groupes/<int:id>', views.groupe_detail, name='groupe-detail'),
    path('formations/', views.formation_list, name='formation-list'),
    path('formations/<int:id>', views.formation_detail, name='formation-detail'),
    path('contact', views.contact, name='contact'),
    path('emailok', views.email_ok, name='email-ok'),
    path('groupe/add', views.groupe_add, name='groupe-add'),
    path('formation/add', views.formation_add, name='formation-add'),
    path('groupe/<int:id>/change', views.groupe_update, name='groupe-update'),
    path('groupe/<int:id>/delete', views.groupe_delete, name='groupe-delete')
    
]
