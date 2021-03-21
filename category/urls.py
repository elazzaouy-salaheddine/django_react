from rest_framework import routers

from .api import CategoryViewSet


router = routers.DefaultRouter()
router.register('categoreis', CategoryViewSet, 'categoreis')

urlpatterns = router.urls
