"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), #encaminha para a url admin
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #O MEDIA_URL indica o endereço inicial ou base para esses arquivos que serão enviados.
    #O MEDIA_ROOT indica onde estão armazenados no servidor, então se você estiver hospedando na aws por exemplo, você deverá especificar primeiro
    #na onde está o seu servidor para depois colocar, mostrar e armazenar as imagens.

