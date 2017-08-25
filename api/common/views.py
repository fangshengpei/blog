#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-28 19:04:03
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
from django.shortcuts import reverse,redirect,render
from django.http import HttpResponse
from utils.captcha.pfscaptcha import Captcha
from django.core.cache import cache#导入缓存 
try:
	from cStringIO import StringIO
except ImportError:
	from io import BytesIO as StringIO

def captcha(request):
	#1想要得到生成的文本和图片文件
	text,image=Captcha.gene_code()
	out=StringIO()
	image.save(out,'png')
	out.seek(0)
	response=HttpResponse(content_type='image/png')
	response.write(out.read())
    #将验证码的数据写入至缓存中,过期时间两分钟
    #cache.set(text,text,120)
	return response