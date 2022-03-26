from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Ticket
from .serializers import *


class TicketView(APIView):
    def get(self, request):
        ticket = Ticket.objects.all()
        serializer = TicketSerializer(ticket, many=True)
        return Response({"ticket": serializer.data})


class TicketAddView(generics.CreateAPIView):
    serializer_class = TicketSerializer


