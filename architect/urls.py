from rest_framework import routers

from .api import ArchitectViewSet


router = routers.DefaultRouter()
router.register('architects', ArchitectViewSet, 'architects')

urlpatterns = router.urls
