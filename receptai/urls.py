from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', login_required(views.AllUserLists.as_view()), name='home'),
    path('<int:id>', login_required(views.list), name='list')
]