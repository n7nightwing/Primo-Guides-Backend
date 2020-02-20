from rest_framework import serializers
from .models import Guide, Game


class GameSerializer(serializers.HyperlinkedModelSerializer):
    games = serializers.HyperlinkedRelatedField(
        view_name='guide_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Artist
        fields = ('name', 'publisher', 'genre', 'guides',)


class GuideSerializer(serializers.HyperlinkedModelSerializer):
    guide = serializers.HyperlinkedRelatedField(
        view_name='game_detail',
        read_only=True
    )

    class Meta:
        model = Guide
        fields = ('title', 'author', 'skill_level', 'content',)
