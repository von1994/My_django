#coding=utf8
from django.db import models
from django.contrib.auth.models import Group
from django.conf import settings
import datetime
from django.utils import timezone

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

class EmailVerifyRecord(models.Model):
    email_choices = (
        ('register', u'注册'),
        ('forget', u'找回密码'),
    )
    code = models.CharField(max_length=20, verbose_name=u'验证码')
    email = models.EmailField(max_length=50, verbose_name=u'邮箱')
    send_type = models.CharField(choices=email_choices, max_length=10, verbose_name=u'验证码类型')
    send_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u'发送时间')
	
    def __unicode__(self):
	    return self.email
    class Meta:
        verbose_name = u'邮箱验证'
        verbose_name_plural = u"邮箱验证"
	
		
class resource_list(models.Model):
    platform_name = models.CharField(blank=True,max_length=20)
    device_name = models.CharField(blank=True,max_length=50)
    device_type = models.CharField(blank=True,max_length=50)
    device_funcation = models.CharField(blank=True,max_length=100)
    STATUS = models.CharField(blank=True,choices=((u'使用中',u'使用中'),(u'未使用',u'未使用')),max_length=10)
    ADDRESS = models.TextField(blank=True,max_length=100)
    IP_INTERNAL = models.CharField(blank=True,max_length=40)
    IP_MDCN = models.CharField(blank=True,max_length=40)
    IP_MANAGE = models.CharField(blank=True,max_length=40)
    POWER = models.CharField(blank=True,max_length=10)
    MEMORY = models.CharField(blank=True,max_length=10)
    CPU = models.CharField(blank=True,max_length=40)
    THREADCOUNT_CPU = models.CharField(blank=True,default='24',max_length=10)
    DISK = models.CharField(blank=True,max_length=20)
    DISK_SSD = models.CharField(blank=True,max_length=20)
    RAID = models.CharField(blank=True,max_length=50)
    VENDORNAME = models.CharField(blank=True,max_length=20)
    MODEL = models.CharField(blank=True,max_length=20)
    SN = models.CharField(blank=True,max_length=50)
    HIGH = models.CharField(blank=True,max_length=10)
    starDatetime_warranty = models.DateField(blank=True)
    endDatetime_warranty = models.DateField(blank=True)
    def __unicode__(self):
        return self.device_funcation


    class Meta:
        ordering = ['id']
        verbose_name = u"资源列表"
        verbose_name_plural = u"资源列表"

class batch_config(models.Model):
    platform_name = models.CharField(blank=True, max_length=20)
    device_type = models.CharField(blank=True, max_length=50)
    device_funcation = models.CharField(blank=True, max_length=100)
    ADDRESS = models.TextField(blank=True, max_length=100)
    IP_INTERNAL = models.CharField(blank=True, max_length=40)
    IP_MDCN = models.CharField(blank=True, max_length=40)
    IP_MANAGE = models.CharField(blank=True, max_length=40)

    def __unicode__(self):
        return 'IP_MDCN is %s, IP_INTERNAL is %s, IP_MANAGE is %s'%(self.IP_MDCN,self.IP_INTERNAL,self.IP_MANAGE)

    class Meta:
        managed = False
        db_table = "batch_config"
        verbose_name = u"批量配置"
        verbose_name_plural = u"批量配置"
        default_permissions = []
