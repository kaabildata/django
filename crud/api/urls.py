from django.urls import path, include
from .views import ItemView, SingleItemView, SingleItemDelete

urlpatterns = [
    path('items/', ItemView.as_view()),
    path('items/<int:pk>', SingleItemView.as_view()),
    path('items/hard/<int:pk>',SingleItemDelete.as_view())
]
