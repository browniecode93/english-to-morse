from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Message
from .serializers import MessageSerializer
from .translate import encrypt

class MessageViewSet(viewsets.ViewSet):

    def list(self, request):
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid()
        serializer.validated_data['morse_msg'] = encrypt(serializer.validated_data['eng_msg'])
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        product = Message.objects.get(id=pk)
        serializer = Message(product)
        return Response(serializer.data)

    def update(self, request, pk=None):
        product = Message.objects.get(id=pk)
        serializer = MessageSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        product = Message.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)