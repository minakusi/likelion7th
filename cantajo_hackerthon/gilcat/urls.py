"""gilcat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

import app_about.views
import app_map.views
import app_account.views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app_about.views.home, name='home'),
    path('about_1/', app_about.views.about_1, name='about_1'),
    path('about_2/', app_about.views.about_2, name='about_2'),

    
    path('login/', app_account.views.login, name='login'),
    path('signup/', app_account.views.signup, name='signup'),
    path('logout/', app_account.views.logout, name='logout'),
    
    path('map_skku/', app_map.views.map_skku, name='map_skku'),
    path('map_skku/<int:key>', app_map.views.each_cat, name='each_cat'),
    path('map_skku/<int:key>/detail', app_map.views.detail_cat, name='detail_cat'),
    path('map_skku/new ', app_map.views.new, name='new'),
    path('map_skku/delete/<int:key>', app_map.views.delete, name='delete'),    
    path('map_skku/delete2/<int:key>', app_map.views.delete2, name='delete2'),

    
    path('map_skku/update/<int:key>', app_map.views.update, name='update'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )



