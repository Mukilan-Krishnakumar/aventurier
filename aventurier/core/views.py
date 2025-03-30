from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from core.models import VocabItem
from core.serializers import VocabItemSerializer


# Create your views here.
def health(request):
    return JsonResponse({"status": "ok"})


class VocabItemList(APIView):
    def get(self, request):
        vocab_items = VocabItem.objects.all()
        serializer = VocabItemSerializer(vocab_items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VocabItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
