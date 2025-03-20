from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import home,TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', home, name='home'),
    path('api/', include(router.urls)),
]
