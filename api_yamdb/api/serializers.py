from django.forms import ValidationError
from rest_framework import serializers
from rest_framework.exceptions import ParseError
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator
from reviews.models import Genre

from reviews.models import Category, Comment, Review, User


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('username', 'email')
        model = User
    
    def validate_username(self, value):
        if value == 'me':
            raise ValidationError('Нельзя использовать это имя пользователя')
        return value


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    verification_code = serializers.CharField()


class UsersSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,
            validators = [ 
            UniqueValidator( 
                queryset=User.objects.all(), 
                message='Такой адрес уже существует в базе' 
            ) 
        ]
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'bio', 'role')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')
    title = serializers.SlugRelatedField(read_only=True,
                                         slug_field='name')

    class Meta:
        model = Review
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Review.objects.all(),
                fields=('title', 'author')
            )
        ]


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')
    review = serializers.SlugRelatedField(read_only=True,
                                          slug_field='text')

    class Meta:
        model = Comment
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'
