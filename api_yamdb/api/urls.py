from rest_framework import routers
from django.urls import include, path

from .views import CategoriesViewSet, GenresViewSet
from . import views

app_name = 'api'
router = routers.DefaultRouter()
router.register('categories', CategoriesViewSet)
router.register('genres', GenresViewSet)
# router.register('titles', TitlesViewSet)
# router.register('titles/(?P<titles_id>\\d+)/reviews', ReviewsViewSet, basename=Reviews)
# router.register('titles/(?P<titles_id>\\d+)/reviews/(?P<reviews_id>\\d+)/comments', CommentsViewSet, basename=Comments)
urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', views.signup),
    path('v1/auth/token/', views.token)
]
