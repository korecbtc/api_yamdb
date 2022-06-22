from rest_framework import routers
from django.urls import include, path

from .views import CategoriesViewSet

app_name = 'api'
router = routers.DefaultRouter()
# Заготовка для прописывания путей
# Сюда добавим пути для роутера
router.register('categories', CategoriesViewSet)
# router.register('genres', GenresViewSet)
# router.register('titles', TitlesViewSet)
# router.register('titles/(?P<titles_id>\\d+)/reviews', ReviewsViewSet, basename=Reviews)
# router.register('titles/(?P<titles_id>\\d+)/reviews/(?P<reviews_id>\\d+)/comments', CommentsViewSet, basename=Comments)

urlpatterns = [
    path('v1/', include(router.urls)),
]
