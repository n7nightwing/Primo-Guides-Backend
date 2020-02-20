from rest_framework import generics
from .serializers import GameSerializer, GuideSerializer
from .models import Game, Guide, User

# Create your views here.


def GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


def GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.ojbects.all()
    serializer_class = GameSerializer


def GuideList(generics.ListCreateAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer


def GuideDetail(generics.ListCreateAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer
