from example.views import AuthorViewSet, BlogViewSet, CommentViewSet, EntryViewSet
from rest_framework import routers

from django.conf import settings
from django.conf.urls import include, url

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'blogs', BlogViewSet)
router.register(r'entries', EntryViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
