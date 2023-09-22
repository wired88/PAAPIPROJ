
from rest_framework import routers, serializers, viewsets

from .models import *


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

    def create(self, validated_data):
        return Contact.objects.create(**validated_data)

    def validate_first_name(self, value):
        if not value.isalpha():  # check for letters
            raise serializers.ValidationError("First Name should contain just letters A-Z.")
        return value

    def validate_last_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Second Name should contain just letters A-Z.")
        return value

    def validate_email(self, value):
        if not "@" in value and not "." in value:
            raise serializers.ValidationError("please provide a valid E-Mail.")
        return value

    def vaaidate_message(self, value):
        if len(value) > 1400:
            raise serializers.ValidationError("A message should be not longer then 1400 characters.")
        elif len(value) <= 20:
            raise serializers.ValidationError("A message should be at least 20 characters long")
        return value


