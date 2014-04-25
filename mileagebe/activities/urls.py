from rest_framework import routers

from activities.views import ActivityViewSet


router = routers.SimpleRouter()
router.register(r'items', ActivityViewSet)
urlpatterns = router.urls
