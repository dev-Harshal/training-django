
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from messenger.models import UserMessages
from atomicloops.pagination import AtomicloopsPagination
from atomicloops.permissions import IsOwnerOrAdminOrReadOnly
from rest_framework import viewsets, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserMessageSerializer
# Create your views here.



class UserMessageView(ModelViewSet):
    queryset = UserMessages.objects.all().order_by('-createdAt')
    # pagination_class = [AtomicloopsPagination]
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserMessageSerializer

    def create(self,request,*args,  **kwargs):
        user=request.user

        msg = UserMessages.objects.create(message=request.data,author=user)
        msg.save()

        serializer = UserMessageSerializer(msg)
        return Response(serializer.data)


    