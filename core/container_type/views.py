from datetime import datetime

from rest_framework import mixins
from rest_framework import generics

from drf_yasg.utils import swagger_auto_schema

from common.filters import RecordIsActiveFilterBackend

from container_type.models import ContainerType

from container_type.serializers import (
    ContainerTypeCreateSerializer,
    ContainerTypeRetrieveSerializer,
    ContainerTypeUpdateSerializer,
    ContainerTypeListSerializer
)


class ContainerTypeCreation(mixins.CreateModelMixin, generics.GenericAPIView):
    
    serializer_class =  ContainerTypeCreateSerializer
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ContainerTypeList(mixins.ListModelMixin, generics.GenericAPIView):
    
    queryset = ContainerType.objects.all()
    
    serializer_class = ContainerTypeListSerializer
    
    filter_backends = [
        RecordIsActiveFilterBackend
    ]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ContainerTypeUpdate(mixins.UpdateModelMixin, generics.GenericAPIView):
    
    queryset = ContainerType.objects.all()
    
    serializer_class = ContainerTypeUpdateSerializer
    
    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class ContainerTypeDetailOrDelete(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = ContainerType.objects.all()
    
    serializer_class = ContainerTypeRetrieveSerializer

    filter_backends = [
        RecordIsActiveFilterBackend
    ]
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

class ContainerTypeSoftDelete(mixins.DestroyModelMixin, generics.GenericAPIView):
    
    queryset = ContainerType.objects.all()
    
    def perform_destroy(self, instance):
        instance.deleted_at = datetime.now()
        instance.is_active = None
        instance.save()
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ContainerTypeBulkSoftDelete(mixins.CreateModelMixin, generics.GenericAPIView):
    
    queryset = ContainerType.objects
    
    def delete(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    