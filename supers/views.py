from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from super_types.models import SuperType
from .serializers import SuperSerializer
from .models import Super
from rest_framework import status

@api_view(['GET', 'POST'])
def super_list(request):

    if request.method == 'GET':
        
        type_param=request.query_params.get('type')
        
        supers = Super.objects.all()
        custom_response = {}

        types = SuperType.objects.all()

        if type_param:
            supers = supers.filter(super_type__type=type_param)
            if type_param:

            


        serializer = SuperSerializer(supers, many=True)
        return Response(custom_response)
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def super_detail(request, pk):
    super = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(super)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
