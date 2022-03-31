from rest_framework import serializers

from .models import *


class TicketSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Ticket
        fields = '__all__'

    # def create(self, validated_data):
    #     return Ticket.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)

