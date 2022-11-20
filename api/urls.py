from django.urls import path
from .views import ItemViewSet, BuyViewSet

urlpatterns = [
    path('buy/<int:pk>/', BuyViewSet.as_view({'get': 'retrieve'})),
    path('item/<int:pk>/', ItemViewSet.as_view({'get': 'retrieve'}))
]
