from rest_framework import routers

from .api import GteProjectsViewSet


router = routers.DefaultRouter()
router.register('gteprojects', GteProjectsViewSet, 'gteprojects')

urlpatterns = router.urls
