from rest_framework import serializers
from rest_framework.exceptions import ParseError
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator
from reviews.models import Review, Comment, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Category


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
