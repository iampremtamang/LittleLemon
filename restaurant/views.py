from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render
from django.contrib.auth.models import User

from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer, UserSerializer


def home(request):
    return render(request, 'index.html')

class MenuView(APIView):
    def get(self, request):
        menu_objs = Menu.objects.all()
        serializer = MenuSerializer(menu_objs, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
        
    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        users = self.queryset
        serializer = self.serializer_class(users, many=True)
        return Response({"status": "success", "data": serializer.data})

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    