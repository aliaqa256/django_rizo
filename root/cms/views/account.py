from django.shortcuts import render,redirect,Http404,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
#from django.contrib.auth.models import User
from django.contrib import messages
from cms.models import *
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from cms.utils import *
from cms.forms.account.forms import ChangeRestPasswordForm,FormProfile,UserLoginForm,UserRegistrationForm,RestPasswordForm,ChangePasswordForm
from django.contrib.auth import get_user_model
from cms.decorators import user_required
User = get_user_model()
#from django.views.decorators.http import require_http_methods
@login_required
def accounthome(request):
    return render(request, 'account/Home.html')

@user_required
def signin(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            f = form.cleaned_data
            user = authenticate(request, email=f['email'], password=f['password'])
            if user: 
                login(request, user)
                return redirect('cms:accounthome')
            else :
                messages.add_message(request, messages.ERROR, 'نام یا کلمه عبور درست وارد نشده','danger')
    else : 
        form = UserLoginForm()
    obj = {
        'form' : form
    }
    return render(request, 'account/Login.html',obj)

@user_required
def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            f = form.cleaned_data
            if f['password'] == f['repassword']:
                user = User.objects.create_user(email=f['email'],password=f['password'])
                user.save()
                messages.add_message(request, messages.SUCCESS, 'اکانت شما ساخته شد','success')
                return redirect('cms:login')
            else :
                messages.add_message(request, messages.ERROR, 'پسورد های وارد شده با هم برابر نیستند','danger')
    else : 
        form = UserRegistrationForm()
    obj = {
        'form' : form
    }
    return render(request, 'account/Signup.html',obj)     

def signout(request):
    logout(request)
    return redirect('cms:login')

@user_required
def restpass(request):
    if request.method == "POST":
        form = RestPasswordForm(request.POST)
        if form.is_valid():
            domain = get_current_site(request)
            email = form.cleaned_data['email']
            if User.objects.filter(email=email):
                if pwsrest.objects.filter(email=email) : 
                    getpws=get_object_or_404(pwsrest,email=email)
                    datepws = getpws.date
                    timepws = getpws.time
                    datenow = timezone.now().date()
                    minpws = fixtimemin(timepws.minute)
                    refreshtime =  minpws - timezone.now().time().minute +1
                    if datenow > datepws:
                        delpws=pwsrest.objects.filter(email=email).delete()
                        if restpassemail(email=email,domain=domain):
                            messages.add_message(request, messages.SUCCESS, 'ایمیل به شما ارسال شد لطفا صندوق دریافت خود را چک کنید','success')
                            return redirect('cms:login')
                    elif timezone.now().time().hour < timepws.hour or timezone.now().time().hour > timepws.hour :
                        delpws=pwsrest.objects.filter(email=email).delete()
                        if restpassemail(email=email,domain=domain):
                            messages.add_message(request, messages.SUCCESS, 'ایمیل به شما ارسال شد لطفا صندوق دریافت خود را چک کنید','success')
                            return redirect('cms:login')
                    elif minpws < timezone.now().time().minute :
                        delpws=pwsrest.objects.filter(email=email).delete()
                        if restpassemail(email=email,domain=domain):
                            messages.add_message(request, messages.SUCCESS, 'ایمیل به شما ارسال شد لطفا صندوق دریافت خود را چک کنید','success')
                            return redirect('cms:login')
                    else :
                        messages.add_message(request, messages.WARNING, f' ایمیل بعدی {refreshtime} دقیقه دیگر ')
                else :
                    if restpassemail(email=email,domain=domain):
                        messages.add_message(request, messages.SUCCESS, 'ایمیل به شما ارسال شد لطفا صندوق دریافت خود را چک کنید','success')
                        return redirect('cms:login')
            else:
                messages.add_message(request, messages.ERROR, 'در وارد کردن ایمیل خود توجه کنید همچین ایمیلی موجود نیست','danger')
    else:
        form = RestPasswordForm()
    obj = {
        'form' : form
    }
    return render(request, 'account/Restpassword.html',obj)
    
@user_required
def subpass(request,uuid):
    getpws=get_object_or_404(pwsrest,uuid=uuid,status=False)
    if request.method == "POST":
        form = ChangeRestPasswordForm(request.POST)
        if form.is_valid():
            f=form.cleaned_data
            if f['password'] == f['repassword'] :
                setpws = get_object_or_404(User,email=getpws.email)
                setpws.set_password(f['password'])
                setpws.save()
                delpws=get_object_or_404(pwsrest,uuid=uuid).delete()
                messages.add_message(request, messages.SUCCESS, 'پسورد با موفقیت تغییر یافت','success')
                return redirect('cms:login')
            else : 
                messages.add_message(request, messages.ERROR, 'کلمه عبور با تکرار خود برابر نیست','danger')
    else :
        form = ChangeRestPasswordForm()
    obj = {
        'form' : form
    }     
    return render(request, 'account/Set_new_password.html',obj)
    
    
@login_required
def changepass(request):
    if request.method == "POST":
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            f = form.cleaned_data
            getuser = get_object_or_404(User,email=request.user.email)
            if getuser.check_password(f['oldpassword']) : 
                if f['password'] == f['repassword'] :
                    getuser.set_password(f['password'])
                    getuser.save()
                    messages.add_message(request, messages.INFO, 'پسورد شما تغییر کرد لطفا دوباره وارد شوید','info')
                    logout(request)
                    return redirect('cms:login') 
                else:
                    messages.add_message(request, messages.ERROR, 'تکرار پسورد با  پسورد جیدید برابر نیست','danger')
            else:
                messages.add_message(request, messages.ERROR, 'پسورد که وارد کرده اید اشتباه است','danger')
    else :
        form = ChangePasswordForm()
    obj = {
        'form' : form
    } 
    return render(request, 'account/Change_Password.html',obj)

@login_required
def profile(request):
    if request.method == "POST":
        form = FormProfile(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'پروفایل شما ابدیت شد','success')
            return redirect('cms:accounthome') 
    else : 
        form = FormProfile(instance=request.user)
    obj = {
        'form' : form
    } 
    return render(request,'account/profile.html',obj)
