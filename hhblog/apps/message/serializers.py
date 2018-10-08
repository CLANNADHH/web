from rest_framework import serializers
from datetime import datetime

from message.models import VipMessage


class MessageSerializer(serializers.ModelSerializer):
    # def create(self,validated_data):
    #     validated_data['message_time'] = datetime.now()
    #     message = super().create(validated_data)
    class Meta:
        model = VipMessage
        fields = "__all__"

    # def create(self, validated_data):
    #     print(validated_data)
    #     return validated_data
