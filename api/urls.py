from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import MovieViewSet,RatingViewSet,UserViewSet
from django.conf.urls.static import static
from django.conf import settings

router=routers.DefaultRouter()
router.register('movies',MovieViewSet)
router.register('ratings',RatingViewSet)
router.register('users',UserViewSet)

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('new/', admin.site.urls),
]
