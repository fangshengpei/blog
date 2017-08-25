#coding:utf-8
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,reverse,redirect
from django.contrib.auth.decorators import login_required
from forms import LoginForm

#登录函数
def cms_login(request):#后台管理登录
	if request.method=='GET':
		return render(request,'cms_login.html')
	else:
		form=LoginForm(request.POST)
		if form.is_valid(): #验证表单
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password')
			user=authenticate(username=username,password=password)#验证用户
			if user:
				login(request,user)
				nexturl=request.GET.get('next') #如果用户没有登录，从其他页面进去，需要进行登录，当登录成功后，在跳转回去，增加用户体验
				#print nexturl
				if nexturl:
					return redirect(nexturl)
				else:#当用户是从登录界面进来的，登录成功后，直接进入首页。
					return redirect(reverse('cms_index'))
			else:
				return render(request,'cms_login.html',{'errors':u'用户名或密码错误'})
		else:
			return HttpResponse(u'用户名不规范')
#登出函数
def cms_logout(request):
	logout(request)
	return redirect(reverse('cms_login'))


#首页
@login_required     #装饰器:登陆之后才能访问首页
def cms_index(request):
	return render(request,'cms_index.html')

@login_required
def cms_add_article(request):
	if request.method=='GET':
		return render(request,'cms_add_article.html')
	else:
		pass