from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DataModel
from .serializers import DataModelsSerializers


# Lists all the data or create a new one
class DataList(APIView):

    def get(self, request):         # take from suyash
        data = DataModel.objects.all()
        serializer = DataModelsSerializers(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DataModelsSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


