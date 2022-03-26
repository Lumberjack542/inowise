from rest_framework import serializers

from .models import *


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = (

            'title',
            'description',
            'completed',
            'frozen',
            'unresolved'
        )

    def create(self, validated_data):
        return Ticket.objects.create(**validated_data)