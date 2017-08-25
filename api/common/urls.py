#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-28 19:03:52
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
from django.conf.urls import url
import views

urlpatterns =  [
url(r'^captcha/$',views.captcha,name='common_captcha'),
]


