from django.urls import path, include
from . import views
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'ticket', views.TicketViewSet, basename='Ticket')

urlpatterns = [

    #path('', views.TicketViewAll.as_view()),
    path('su/', views.TicketViewAdmin.as_view({'get': 'list', 'post': 'create'})),
    path('su/<int:pk>/', views.TicketViewAdmin.as_view({'put': 'update', 'delete': 'destroy', 'get': 'retrieve'})),
    path('post/', views.TicketForUser.as_view()),


]