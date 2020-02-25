from rest_framework import generics
from .serializers import GuideSerializer, GameSerializer, UserSerializer
from .models import Game, Guide, User

# Create your views here.


class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GuideList(generics.ListCreateAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer


class GuideDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
