from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser

from .serializers import CodeRunSerializer
from .PlainTextParser import PlainTextParserClass
from . import solution

class CodeRunApiView(APIView):

	parser_classes = (PlainTextParserClass,)

	def post(self, request, format=None):
		
		values = request.data.split('\n')
		results = []
		print(len(values))
		for i in range(1,len(values),2):
			a=values[i]
			b=values[i+1]
			results.append(str(solution.main(a,b)))

		return Response({'received data': results})