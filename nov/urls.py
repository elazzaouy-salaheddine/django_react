from rest_framework import routers

from .api import NovProjectsViewSet


router = routers.DefaultRouter()
router.register('novprojects', NovProjectsViewSet, 'novprojects')

urlpatterns = router.urls
