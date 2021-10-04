from django.shortcuts import render,redirect
from cms.models import *
from django.http import Http404,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.



def blog_list_view(request):

    query=Blog.objects.active_Blogs()

    menus=menu.objects.all()

    if query is None:
        print("not article")
        raise Http404("no post here")
    query=query.order_by("-publish_time")
    context={
        "blog":query,
        'menus':menus
    }

    return render(request,"blog/blog_list_view.html",context)


def blog_detail_view(request, slug):
    detail_query=Blog.objects.get_by_slug(slug=slug)



    
    if detail_query is None:
        raise Http404("there is no article here")
    qs_comment=Blog.objects.get(slug=slug)
    comments=qs_comment.comments.all().order_by("-posted_time")
    
    ######FOR TAGS
    my_blog = Blog.objects.filter(slug=slug)
    
    ####inja post ro gerfetam rikhtam to my blog
    index_my_blog = list(my_blog)[0]
    ####tamamtag haye poste ro gereftam
    tags_to_page = list(index_my_blog.my_tags.all())



    context={
        
        "blog":detail_query,
        "tags_to_page":tags_to_page,
        "comments":comments,
      
    }

    if detail_query is None:

        raise Http404()


    print(detail_query[0].seen) 
    qs_comment.seen += 1
    print(detail_query[0].seen )

    
    qs_comment.save() 
    


    return render(request,"blog/blog_detail_view.html",context)


###in func mibare besafhe ii ke blog haei k on tago drn neshoon mide
def blog_tag(request,slug):
    tag_get=Tag.objects.get_by_slug(slug=slug)
    if tag_get is None:
        return Http404("in tag vojood nadarad")

    qs = Blog.objects.filter(active=True, my_tags=tag_get).order_by("created_time")





    context={
        "blogs":qs
    }
    return render(request,"blog/blog_tags_veiw.html",context)



def blog_category(request,slug):
    cat_get=Category.objects.get(slug=slug)

    qs = Blog.objects.filter(active=True, category=cat_get).order_by("-time")





    context={
        "blogs":qs
    }
    return render(request,"blog/blog_tags_veiw.html",context)




@login_required(login_url="/Signin/")
def blog_star(request,slug):
    blog=Blog.objects.get(slug=slug)
    stared=False
    if blog.star.filter(id=request.user.id).exists():
        blog.star.remove(request.user)
        stared=False
    else:
        blog.star.add(request.user)
        stared=True

    
    return HttpResponseRedirect(reverse('cms:blog_detail',kwargs={'slug':blog.slug}))







@login_required(login_url="/Signin/")
def blog_comment(request,slug):
    blog=Blog.objects.get(slug=slug)
    user=request.user
    text=request.POST.get("comment_post")
    model_comment=CommentBlog.objects.create(blog=blog,text=text,sender=user)

    return HttpResponseRedirect(reverse('cms:blog_detail',kwargs={'slug':blog.slug}))











@login_required(login_url="/Signin/")
def blog_comment_like(request,id):
    comment=CommentBlog.objects.get(id=id)
    if comment.like.filter(id=request.user.id).exists():
        comment.like.remove(request.user)
        stared=False
    else:
        comment.like.add(request.user)
        stared=True
        if comment.dislike.filter(id=request.user.id).exists():
            comment.dislike.remove(request.user)
       


    
    return HttpResponseRedirect(reverse('cms:blog_detail',kwargs={'slug':comment.blog.slug}))
@login_required(login_url="/Signin/")
def blog_comment_dislike(request,id):
    comment=CommentBlog.objects.get(id=id)
    if comment.dislike.filter(id=request.user.id).exists():
        comment.dislike.remove(request.user)
        stared=False
    else:
        comment.dislike.add(request.user)
        stared=True
        if comment.like.filter(id=request.user.id).exists():
            comment.like.remove(request.user)

    
    return HttpResponseRedirect(reverse('cms:blog_detail',kwargs={'slug':comment.blog.slug}))



def blog_search(request):
    q=request.GET.get("q")
    if q is not None:

       blog=Blog.objects.search(q)
    else:
        blog=Blog.objects.active_Blogs()

    context={
        "blog":blog
    }

    return render(request,"blog/blog_list_view.html",context)