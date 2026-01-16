from rest_framework import serializers
from .models import Post, Comments, Like, CustomUser


### === POST === ###
class GetPostsListSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'author', 'date']


class CreatePostsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'description']
        read_only_fields = ['id']  # author не передається, додається в perform_create()


class DeletePostsListSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'author', 'date']


class PutPostsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'description']
        read_only_fields = ['id']


class PatchPostsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'description']
        read_only_fields = ['id']


class GetPostOneUserSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'author', 'date']


### === COMMENTS === ###
class GetCommentListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comments
        fields = ['id', 'text_comments', 'date', 'user', 'post']


class CreateCommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'text_comments', 'post']
        read_only_fields = ['id']  # user додається через perform_create()


class DeleteCommentListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comments
        fields = ['id', 'text_comments', 'date', 'user', 'post']


class PutCommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'text_comments', 'post']
        read_only_fields = ['id']


class PatchCommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'text_comments']
        read_only_fields = ['id']


### === LIKES === ###
class GetAllUserLikeSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Like
        fields = ['id', 'author', 'post']


class CreateUserLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id']
        read_only_fields = ['id']  # user призначається через perform_create()


class DeleteUserLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'post']
        read_only_fields = ['id']


### === USERS === ###
class GetCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'email', 'date_joined', 'first_name', 'last_name', 'last_login', 'is_active', 'is_staff', 'is_superuser', ]


class CreateCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class DeleteCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email']


class PutCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        password = validated_data.get('password')
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class PatchCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        password = validated_data.get('password')
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class GetMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'is_staff', 'is_superuser', 'date_joined', 'last_login', 'is_active', 'first_name', 'last_name', 'password']


class LoginCustomUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

