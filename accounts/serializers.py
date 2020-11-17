from rest_framework import serializers

from django.contrib.auth import get_user_model

User = get_user_model()


class AccountCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'avatar']

    def validate_username(self, username):
        if len(User.objects.filter(username=username)) > 0:
            raise serializers.ValidationError(f"User with username '{username}' already exists")
        return username


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'avatar']
        read_only_fields = ['id']
