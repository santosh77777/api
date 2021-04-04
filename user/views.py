from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins, generics
from .serializers import *

User = get_user_model()

class RegisterView(mixins.CreateModelMixin,
                  generics.GenericAPIView):
    serializer_class = UserCreateSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ShiftGet(mixins.ListModelMixin, generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



class ShiftPost( mixins.CreateModelMixin,
                  generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)