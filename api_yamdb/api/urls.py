from django.urls import include, path
from rest_framework import routers

from .views import GenresViewSet, UsersViewSet

from . import views
from .views import CategoriesViewSet, CommentViewSet, ReviewViewSet

app_name = 'api'
router = routers.DefaultRouter()
router.register('categories', CategoriesViewSet)
router.register('genres', GenresViewSet)
router.register('users', UsersViewSet)
# router.register('titles', TitlesViewSet)
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='Reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='Comments'
)
urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', views.signup),
    path('v1/auth/token/', views.token)
]
