from rest_framework import serializers
from .models import User

# User -> id, name, email, gender , city
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'gender', 'city')
        