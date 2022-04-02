from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.ReceptasList.as_view(), name='receptai'),
    path('<int:pk>', views.ReceptasDetail.as_view(), name='receptas_detail')
]