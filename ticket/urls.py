from django.urls import path
from . import views

urlpatterns = [
    path('', views.TicketView.as_view(), name='main'),
    path('add/', views.TicketAddView.as_view(), name='add_ticket')
]