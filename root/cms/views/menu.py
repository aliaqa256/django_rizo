from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from cms.models import *
import codecs
from django.template import loader
from django.conf import settings

def menus(request,page):
    menuadr = get_object_or_404(menu,name=page)
    menuf= menuadr.file.all().order_by("-date")[:1]
    #html = ''
    pk = None
    if menuf:
        for m in menuf:
            pk = m.pk
        gettemplate = templatedir.objects.get(pk=pk)
        #pagep = str(settings.BASE_DIR) +'\\template\\'+str(gettemplate.file)
        #file = codecs.open(str(pagep), "r","UTF-8")
        #html=file.readlines()
        address= 'page/'+str(gettemplate.file)
        template = loader.get_template(address)
    else : 
        return HttpResponseRedirect(menuadr.link) 
    return HttpResponse(template.render())
    