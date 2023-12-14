from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import Group,User
from django.contrib.auth.decorators import login_required
from bloodstock.models import BloodStock
from users.decorators import allowed_users

