from django.shortcuts import render
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import CountrySerializer, CountryUpdateSerializer
from .models import Country


# Create your views here.
class CountryViewset(GenericViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()

    def get_serializer_class(self):
        if self.action == 'ban' or self.action == 'bulk_ban':
            return CountryUpdateSerializer
        return CountrySerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(methods=['PATCH'], detail=True)
    def ban(self, request, pk):
        country = self.get_object()
        serializer = self.get_serializer(country, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)

    @action(methods=['PATCH'], detail=False, url_path='bulk-ban')
    def bulk_ban(self, request):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        for data in request.data:
            country = Country.objects.get(pk=data['id'])
            serial = self.get_serializer(country, data=data)
            serial.is_valid()
            serial.save()
        return Response(status=status.HTTP_200_OK)
