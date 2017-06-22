# -*- coding: utf-8 -*-
import xadmin
from .models import resource_list, EmailVerifyRecord,batch_config
from xadmin import views
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from xadmin.plugins.inline import Inline
from xadmin.plugins.batch import BatchChangeAction,BatchConfigAction


class MainDashboard(object):
    widgets = [
        [
            {"type": "qbutton", "title": "Quick Start", "btns": [{'model': resource_list}, {'model': EmailVerifyRecord}, {'title': "Baidu", 'url': "http://www.baidu.com"}, {'title': "Baidu2", 'url': "http://www.baidu.com"}]},
        ]
    ]
xadmin.sites.site.register(views.website.IndexView, MainDashboard)
 
class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']
    reversion_enable = True
 
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)

class batch_configAdmin(object):
    list_display = (
    'platform_name', 'device_type', 'device_funcation', 'ADDRESS', 'IP_MDCN', 'IP_INTERNAL', 'IP_MANAGE')
    list_filter = []
    list_export = []
    show_bookmarks = False
    actions = [BatchConfigAction,]

xadmin.site.register(batch_config,batch_configAdmin)

class resource_listAdmin(object):
	
    wizard_form_list = [
        (u'设备信息', ('platform_name','device_name','device_type','device_funcation','STATUS','ADDRESS','VENDORNAME','MODEL','SN','HIGH')),
        (u'IP信息', ('IP_INTERNAL','IP_MDCN','IP_MANAGE')),
        (u'服务器硬件信息', ('POWER','MEMORY','CPU','THREADCOUNT_CPU','DISK','DISK_SSD')),
		(u'保修起止时间',('starDatetime_warranty','endDatetime_warranty'))
    ]
    
    list_display = ('platform_name','device_funcation','STATUS','ADDRESS','IP_MDCN','MEMORY','CPU','THREADCOUNT_CPU')
    list_filter = ['starDatetime_warranty']
    search_fields = ['device_type','STATUS','device_funcation']
    date_hierarchy = ['starDatetime_warranty']
    list_editable = ['STATUS','ADDRESS','IP_INTERNAL','IP_MDCN','IP_MANAGE','DISK','DISK_SSD','starDatetime_warranty','endDatetime_warranty']
    show_detail_fields = ['ADDRESS']
    relfield_style = 'fk-select'
    reversion_enable = True
    actions = [BatchChangeAction, ]
    batch_fields = ('platform_name','device_name','device_type','device_funcation','STATUS','ADDRESS','VENDORNAME','MODEL','SN','HIGH','IP_INTERNAL','IP_MDCN','IP_MANAGE','POWER','MEMORY','CPU','THREADCOUNT_CPU','DISK','DISK_SSD','starDatetime_warranty','endDatetime_warranty')




xadmin.site.register(resource_list,resource_listAdmin)


 
class BaseSetting(object):
    enable_themes = False
    use_bootswatch = True
 
xadmin.site.register(views.BaseAdminView, BaseSetting)

class GlobalSetting(object):
    site_title = u'资源管理平台'
    site_footer = u'敏捷小小组'
    global_search_models = [resource_list]
    global_models_icon = {
        resource_list: 'fa fa-laptop',
        EmailVerifyRecord: 'fa fa-cloud'
    }
    menu_style = u'default'#'accordion'
    def get_site_menu(self):
        return(
            {'title': u'资源管理', 'perm': self.get_model_perm(resource_list, 'change'), 'menus':(
                {'title': u'邮箱验证', 'icon':'fa fa-envelope',  'url': self.get_model_url(EmailVerifyRecord, 'changelist')},
                {'title': u'资源总览', 'icon':'fa fa-picture-o', 'url': '/app/overview'},
		{'title': u'资源列表', 'icon':'fa fa-list', 'url': self.get_model_url(resource_list, 'changelist')},
		{'title': u'批量配置', 'icon':'fa fa-pencil', 'url':self.get_model_url(batch_config, 'changelist')}
            )},
        )

 
xadmin.sites.site.register(views.CommAdminView, GlobalSetting)


#from xadmin.sites import site
#from xadmin.views import BaseAdminView
#
#class MyAdminView(BaseAdminView):
#    def get(self, request, *args, **kwargs):
#        pass
#site.register_view(r'^me_test/$', MyAdminView, name='my_test')

#from xadmin.plugins.actions import BaseActionView
#
#from xadmin.views.base import ModelAdminView, filter_hook, csrf_protect_m
# 
#
#class MyAction(BaseActionView):
#
#    # 这里需要填写三个属性
#    action_name = "my_action"    #: 相当于这个 Action 的唯一标示, 尽量用比较针对性的名字
#    description = u'Test selected %(verbose_name_plural)s'
#
#    model_perm = 'change'    #: 该 Action 所需权限
#
#    # 而后实现 do_action 方法
#    def do_action(self, queryset):
#        # queryset 是包含了已经选择的数据的 queryset
#        for obj in queryset:
#            # obj 的操作
#            pass
#        # 返回 HttpResponse
#        return HttpResponse('Nothing')
#		
#class MyModelAdmin(object):
#
#    actions = [MyAction, ]
