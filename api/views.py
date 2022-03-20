from django.http import Http404
from .serializers import ReceptasSerializer
from receptai.models import Receptas
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class ReceptasList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        data = Receptas.objects.all()
        serializer = ReceptasSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReceptasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReceptasDetail(APIView):
    """
    Retrieve, update or delete a todoList instance.
    """
    def get_object(self, pk):
        try:
            return Receptas.objects.get(id=pk)
        except Receptas.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        data = self.get_object(pk)
        serializer = ReceptasSerializer(data)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        existing_list = self.get_object(pk)
        serializer = ReceptasSerializer(existing_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        data = self.get_object(pk)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)