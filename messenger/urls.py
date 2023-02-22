from django.urls import path
from rest_framework.routers import DefaultRouter
from messenger.views import UserMessageView

router = DefaultRouter()
router.register("user-messages",UserMessageView,basename="user-messages")
urlpatterns = router.urls
    