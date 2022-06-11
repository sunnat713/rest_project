
from django.urls import path
from . import views
urlpatterns = [
    path('<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path('<int:pk>/update/', views.ProductUpdate.as_view(), name='product-edit'),
    path('<int:pk>/delete/', views.ProductDeleteView.as_view()),
    path('', views.ProductListCreateAPIView.as_view(), name='product-list'),

]


