from rest_framework import routers
from django.urls import include, path

app_name = 'api'
router = routers.DefaultRouter()
# Заготовка для прописывания путей
# Сюда добавим пути для роутера


urlpatterns = [
    path('v1/', include(router.urls)),
]
