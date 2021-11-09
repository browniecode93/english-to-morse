from rest_framework import serializers
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["id", "eng_msg", "morse_msg"]  # and whatever other fields you want to expose
        extra_kwargs = {"morse_msg": {"required": False, "allow_null": True}}
