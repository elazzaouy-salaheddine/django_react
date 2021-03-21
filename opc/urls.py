from rest_framework import routers

from .api import OpcViewSet


router = routers.DefaultRouter()
router.register('opcs', OpcViewSet, 'opcs')

urlpatterns = router.urls
