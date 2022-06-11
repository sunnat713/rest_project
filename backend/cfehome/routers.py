from rest_framework.routers import DefaultRouter

from product.viewsets import ProductGenericViewSet
router = DefaultRouter()
router.register('product', ProductGenericViewSet, basename='product')
urlpatterns = router.urls
