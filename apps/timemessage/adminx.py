# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     adminx
   Description :
   Author :       wsm
   date：          2019-03-11
-------------------------------------------------
   Change Activity:
                   2019-03-11:
-------------------------------------------------
"""
__author__ = 'wsm'

import xadmin
from xadmin import views

from .models import Detail, SourceVideo, SourceImg

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = '地理与历史管理系统'
    site_footer = '地理与历史'
    menu_style = "accordion"


class DetailAdmin(object):
    pass

class SourceVideoAdmin(object):
    pass

class SourceImgAdmin(object):
    pass

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(Detail, DetailAdmin)
xadmin.site.register(SourceVideo, SourceVideoAdmin)
xadmin.site.register(SourceImg, SourceImgAdmin)
