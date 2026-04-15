from rest_framework import serializers

from ..models import CustomUser, Post


class GetCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'description', 'avatar', 'email', 'date_joined', 'first_name', 'last_name',
                  'last_login', 'is_active', 'is_staff', 'is_superuser']


class CreateCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class UpdateCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username", 'description', 'avatar', "email", "first_name", "last_name", "password"]
        extra_kwargs = {
            "username":    {"required": True},
            "description": {"required": True},
            "avatar":      {"required": True},
            "email":       {"required": True},
            "first_name":  {"required": True},
            "last_name":   {"required": True},
            "password":    {"write_only": True, "required": False},
        }

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)

        instance.save()
        return instance


class GetPostOneUserSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'img', 'author', 'date']


class GetMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'avatar', 'email', 'is_staff', 'is_superuser', 'date_joined', 'last_login',
                  'is_active', 'first_name', 'last_name', 'password']


class LoginCustomUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
