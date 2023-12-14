from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count, Q
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from enfermaria.models import BloodRequest

class APINotifBadge(APIView):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request, format=None):
		obj1 = BloodRequest.objects.filter(is_sent=True, is_approved=False).all().count()
		objects = obj1
		return Response({'value':objects})

class APINotifBloodRequest(APIView):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request, format=None):
		objects = BloodRequest.objects.filter(is_sent=True, is_approved=False).all().count()
		return Response({'value':objects})

