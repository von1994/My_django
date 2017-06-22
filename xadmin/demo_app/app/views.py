# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponse,Http404
from django.views.decorators.csrf import csrf_exempt
from app.models import resource_list
import json
import write
import read
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return HttpResponse('Hello, this is a index page!')

def overview(request):
    using = len(resource_list.objects.filter(STATUS="使用中"))
    unused = len(resource_list.objects.filter(STATUS="未使用"))
    platform_volte = len(resource_list.objects.filter(platform_name="VoLTE"))
    platform_lte = len(resource_list.objects.filter(platform_name="LTE"))
    platform_fast = len(resource_list.objects.filter(platform_name="FAST"))
    return render_to_response('overview.html',{'using':using,'unused':unused,'platform_volte':platform_volte,'platform_lte':platform_lte,'platform_fast':platform_fast})

@csrf_exempt
def configure(request):
    json_data = request.POST
    ip_list = json_data.getlist('IP_MDCN[]')
    flag = 0
    for i in ip_list:
        if i == u'无' or i == u'\u65e0':
            flag = 1
            break
        else:
            pass
    if flag:
        ip_list = json_data.getlist('IP_INTERNAL[]')
    else:
        pass
    write.writeIntoTxt(IP_list=ip_list,fullpathOftxt='/home/feng/test.txt',flag='[tmp]')
    return HttpResponse()
    #return HttpResponse('It is bg ,data is %s'%json_data.dict()['IP_MDCN[]'])

@csrf_exempt
def sendemail(request):
    tomail = request.POST['email']
    send_mail('subject', 'body', 'hndev_ops@163.com', [tomail], fail_silently=True)
    return HttpResponse('send OK')

def ipinfo(request):
    #read.ReadFromTxt('/home/feng/test.txt')
    return HttpResponse(read.ReadFromTxt('/home/feng/test.txt'))

def step1(request):
    return render_to_response('step1.html',{})
