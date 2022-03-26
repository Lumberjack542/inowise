from django.urls import path
from . import views

urlpatterns = [
    path('', views.TicketView.as_view(), name='main'),
    path('update/<int:pk>/', views.TicketUpdate.as_view(), name='add_ticket'),
    path('detail/<int:pk>/', views.TicketDetailView.as_view(), name='det'),

]