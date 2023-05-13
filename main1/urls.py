from . import views
from django.urls import path

urlpatterns = {
    path('', views.welcome_view, name='wh'),
}
