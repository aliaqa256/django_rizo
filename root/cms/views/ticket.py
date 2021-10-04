from django.shortcuts import render,get_object_or_404,redirect
from cms.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from cms.forms.ticket.forms import NewTicketForm,TicketForm

@login_required
def myticket(request):
    chanels = chanel.objects.filter(createor=request.user.id).order_by("-date")
    obj={
        'chanels':chanels,
    }
    return render(request, 'account/ticket/chanels.html',obj)
    
@login_required
def myticketchanel(request,token):
    chanels = get_object_or_404(chanel,token=token,createor=request.user.id)
    tickets = ticket.objects.filter(chanel=chanels).order_by("-date")
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            des = form.cleaned_data['des']
            createticket = ticket.objects.create(chanel=chanels,sender=request.user.email,des=des)
            messages.add_message(request, messages.SUCCESS, 'تیکت شما ثبت شد','success')
            return redirect('cms:myticketchanel',token=token)
    else :
        form = TicketForm()
    obj={ 
        'form':form,
        'chanels':chanels,
        'tickets':tickets,
    }
    return render(request, 'account/ticket/tickets.html',obj)

@login_required
def newticket(request):
    if request.method == "POST":
        form = NewTicketForm(request.POST)
        if form.is_valid():
            f = form.cleaned_data
            import uuid
            uuid = uuid.uuid4()
            createchanel = chanel.objects.create(token=uuid,title=f['choice'])
            createchanel.createor.add(str(request.user.id))
            createticket = ticket.objects.create(chanel=createchanel,sender=request.user.email,title=f['title'],mozoee=f['mozoee'],des=f['des'])
            messages.add_message(request, messages.SUCCESS, 'تیکت شما ثبت شد','success')
            return redirect('cms:myticket')
    else : 
        form = NewTicketForm()
    obj={
        'form':form
    }
    return render(request, 'account/ticket/newticket.html',obj)
    
