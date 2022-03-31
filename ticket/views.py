from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from rest_framework import generics, viewsets, mixins
from rest_framework.authentication import TokenAuthentication

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Ticket
from .permissions import IsAdminOrReadOnly
from .serializers import *

# класс для работы админа (должен быть авторизован через токен и сессии )


class TicketViewAdmin(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (IsAdminOrReadOnly,)
    #authentication_classes = (TokenAuthentication,)


class TicketForUser(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

# class TicketViewAll(APIView):
#     def get(self, request):
#         ticket = Ticket.objects.all()
#         serializer = TicketSerializer(ticket, many=True)
#         return Response(serializer.data)
