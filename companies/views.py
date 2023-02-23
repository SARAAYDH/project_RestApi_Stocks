from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import stock
from .serializers import stockserilzers

# Create your views here.
class StockList (APIView):
	def get(self,request):
		stocks=stock.objects.all()
		serializers=stockserilzers(stocks,many=True)
		return Response(serializers.data)
	def post(self):
		pass