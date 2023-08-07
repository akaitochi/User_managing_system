from django.urls import include, path
from .views import login, signup, token, UserViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', login, name='login'),
    path('auth/signup/', signup, name='signup'),
    path('auth/token/', token, name='token'),
]