from rest_framework.routers import DefaultRouter
from users.api import UserAPISet

router = DefaultRouter()
router.register("", UserAPISet, basename="users")
urlpatterns = router.urls
