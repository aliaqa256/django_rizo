from django.shortcuts import render,redirect
from cms import models
from django.http import Http404,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from cms.utils import Shortner


def short_url_post(request):
    
    long=request.POST.get("long")
    print(long[0:4])

    
    if long[0:4] == ("http" or "HTTP")  :

        long=long
    else:

        print(long)
        long="http://"+long
    
        


        





    ismodel=models.ShortUrls.objects.filter(long=long).exists()
    if ismodel:
        
        short=models.ShortUrls.objects.get(long=long).short
        
    else:
        try:

            short=Shortner().issue_token()
            models.ShortUrls.objects.create(long=long,short=short)

        except:
            short=Shortner().issue_token()
            models.ShortUrls.objects.create(long=long,short=short)


    return render(request,"shorturl/shorturl.html",{"short":short})




def show(request,token):
    long=models.ShortUrls.objects.filter(short=token)[0]

    return redirect(long.long)








def short_url_make(request):





    return render(request,"shorturl/shorturl.html")