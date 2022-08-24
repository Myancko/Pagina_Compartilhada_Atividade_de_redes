"""Site_Compartilhado URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from Branch.views import home, jonathan, Moises, Carlitos, Carlitos1, Carlitos2, Carlitos3, Carlitoscao

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', home),
    path('home/', home, name= "home"),
    path('jonathan/', jonathan, name= "jonathan"),
    path('carlos/', Carlitos, name= "carlos"),
    path('carlos1/', Carlitos1, name= "carlos1"),
    path('carlos2/', Carlitos2, name= "carlos2"),
    path('carlos3/', Carlitos3, name= "carlos3"),
    path('carloscao/', Carlitoscao, name= "carloscao"),
    path('moises/', Moises, name= "moises"),
    #path('moises/', Carlitos, name= "moises"),

]
