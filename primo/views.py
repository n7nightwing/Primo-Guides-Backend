from rest_framework import generics
from .serializers import GameSerializer, GuideSerializer
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


class GuideDetail(generics.ListCreateAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer
