from django.shortcuts import render

from rest_framework import generics

from .models import IncomeStatement
from .serializers import IncomeStatementSerializer

# Create your views here.
class IncomeStatementList(generics.ListCreateAPIView):
    queryset = IncomeStatement.objects.all()
    serializer_class = IncomeStatementSerializer

class IncomeStatementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IncomeStatement.objects.all()
    serializer_class = IncomeStatementSerializer
