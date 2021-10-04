from django.shortcuts import redirect

def user_required(view_func):
    def wrap(request, *args, **kwargs):
        try:
            if request.user.email:
                return redirect('cms:accounthome')
        except:
            return view_func(request, *args, **kwargs)        
    return wrap