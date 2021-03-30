"""arqabs URL Configuration

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
from django.urls import include, path

urlpatterns = [
    # path() has 4 args: 2 required (route, view), 2 optional (kwargs, name)
    # route -> URL pattern string
    # view -> calls the specified view function with an HttpRequest object as first argument
    # kwargs -> dic with arbitraty keywords arguments
    # name ->  allows unambiguos ref to this URL
    path('admin/', admin.site.urls),
    path('retratos/', include('retratos.urls')),
]
