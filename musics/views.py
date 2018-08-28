from django.shortcuts import render

from musics.models import Music
from musics.serializers import MusicSerializer
from rest_framework import viewsets

# For Authentications
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class MusicViewSet(viewsets.ModelViewSet):
  queryset = Music.objects.all()
  serializer_class = MusicSerializer
  
  # For Authentications
  permission_classes = (IsAuthenticated,)