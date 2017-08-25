#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-25 20:58:41
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os

from django.conf.urls import url
import views

urlpatterns = [
	url(r'^$',views.cms_index,name='cms_index'),
    url(r'^login/$', views.cms_login,name='cms_login'),
    url(r'^logout$',views.cms_logout,name='cms_logout'),
    url(r'^add_article$',views.cms_add_article,name='cms_add_article')
]
