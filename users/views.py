from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.forms import UserCreationForm
def LogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('learn:index'))

def register(request):
    if request.method !='POST':
        #建一个空表单
        form = UserCreationForm()
    else:
        #获取用户名，密码，注册
        #自动登录
        #从定向到首页登录状态
        form = UserCreationForm(request.POST)
        if form.is_valid():
            newform = form.save()
            print('newform',newform)
            # 让用户自动登录，再重定向到主页
            authenticated_user = authenticate(username=newform.username,password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learn:index'))
    content={'form':form}
    return render(request,'users/register.html',content)



