from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import CreateNewCarView, CarsListView, CarDetailView, CarUpdateView, CarDeleteView
from accounts.views import register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls), #encaminha para a url admin
    path('register/', register_view, name='register'),
    path('cars/', CarsListView.as_view(), name='cars_list'),
    path('new_car/', CreateNewCarView.as_view(), name='new_car'),
    path('logout/', logout_view, name='logout'),
    path('', CarsListView.as_view(), name='home'),
    path('login/', login_view, name='login'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('car/<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),
    path('car/<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #O MEDIA_URL indica o endereço inicial ou base para esses arquivos que serão enviados.
    #O MEDIA_ROOT indica onde estão armazenados no servidor, então se você estiver hospedando na aws por exemplo, você deverá especificar primeiro
    #na onde está o seu servidor para depois mostrar e armazenar as imagens.

