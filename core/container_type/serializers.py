from rest_framework import serializers
from container_type.models import ContainerType

  
class ContainerTypeListSerializer(serializers.ModelSerializer):  
    # TODO: add constraints 
  
    class Meta:  
        model = ContainerType
        fields = ('__all__')


class ContainerTypeRetrieveSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ContainerType
        fields = ('__all__')


class ContainerTypeCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ContainerType
        fields = ('name', 'tenant_id')


class ContainerTypeUpdateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=64, required=False)
    tenant_id = serializers.IntegerField(required=False)
    
    
    class Meta:
        model = ContainerType
        fields = ('name', 'tenant_id')