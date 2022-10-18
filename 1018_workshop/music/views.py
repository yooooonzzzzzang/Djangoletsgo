from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import MusicListSerializer, MusicSerializer,ArtistSerializer, ArtistListSerializer
from .models import Artist, Music
from django.shortcuts import get_object_or_404, get_list_or_404

# Create your views here.

@api_view(['GET', 'POST'])
def artist_list(request):
    if request.method == 'GET':
        artists = get_list_or_404(Artist)
        serializer = ArtistListSerializer(artists, many=True)
        return Response(serializer.data)

    elif request.method=='POST':
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    if request.method == 'GET':
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)


@api_view(['POST'])
def music_create(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = MusicSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(artist=artist)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def music_list(request):
    if request.method =='GET':
        music = get_list_or_404(Music)
        serializer = MusicListSerializer(music, many=True)
        return Response(serializer.data)


@api_view(['GET','PUT','DELETE'])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    if request.method=='GET':
        serializer = MusicSerializer(music)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer = MusicSerializer(music, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method=='DELETE':
        music.delete()
        return Response({'id': music_pk})
