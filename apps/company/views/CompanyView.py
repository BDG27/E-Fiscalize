from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
import json, os, sys

class Company():

    def index(req):
        return render(req, 'company/index.html', {
            
        })