from rest_framework.generics import RetrieveDestroyAPIView, RetrieveUpdateAPIView, ListCreateAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from .models import Item
from .serializers import ItemSerializer


class ItemView(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def create(self, serializer):
        return serializer.save(author='admin')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class SingleItemView(RetrieveUpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class SingleItemDelete(RetrieveDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
