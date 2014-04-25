from rest_framework import routers

from gear.views import GearViewSet


router = routers.SimpleRouter()
router.register(r'items', GearViewSet)
urlpatterns = router.urls
