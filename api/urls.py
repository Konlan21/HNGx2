from django.urls import path
from api.views import PersonViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', PersonViewSet, basename='person')

urlpatterns = router.urls