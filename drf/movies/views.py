from django.shortcuts import render
from rest_framework import viewsets
from .models import Moviedata
from .serializers import MovieSerializer


# Create your views here.
class MovieView(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = MovieSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(category='Action')
    serializer_class = MovieSerializer
