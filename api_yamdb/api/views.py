from django.shortcuts import render
from reviews.models import Review, Comment
from rest_framework import viewsets


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    


