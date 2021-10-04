from django.urls import path,include
import cms.views.blog as blog
import cms.views.shorturl as sl
from cms.views.account import *
from cms.views.menu import *
from cms.views.ticket import *
app_name ="cms"
urlpatterns = [
    path("Home/", accounthome, name="accounthome"),
    path("Signin/", signin, name="login"),
    path("Signup/", signup, name="signup"),
    path("Logout/", signout, name="logout"),
    path("Profile/", profile, name="profile"),
    path("Rest-Password/", restpass, name="restpass"),
    path("Change-Password/", changepass, name="changepass"),
    path("Rest-Password/<uuid:uuid>/", subpass, name="subpass"),
    path("blog/",blog.blog_list_view,name="blog_list"),
    path('blog/<slug>/', blog.blog_detail_view,name="blog_detail"),
    path('blog/tag/<slug>', blog.blog_tag,name="blog_tag"),
    path('blog/cat/<slug>', blog.blog_category,name="blog_category"),
    path('blog/star/<slug>', blog.blog_star,name="blog_star"),
    ############comments
    path('blog/comment/<slug>', blog.blog_comment,name="blog_comment"),
    path('blog/comment/like/<id>', blog.blog_comment_like,name="blog_comment_like"),
    path('blog/comment/dislike/<id>', blog.blog_comment_dislike,name="blog_comment_dislike"),
    #MENU
    path("myticket/", myticket, name="myticket"),
    path("myticket/<uuid:token>/",myticketchanel, name="myticketchanel"),
    path("newticket/",newticket, name="newticket"),
    ##shorturl
    path('sl/make', sl.short_url_make,name="short_url_make"),
    path('sl/post', sl.short_url_post,name="short_url_post"),
    path('sl/show/<str:token>', sl.show, name="show"),
    ##search
    path('search', blog.blog_search,name="blog_search"),
    
]
# menu or raise 404
urlpatterns +=[
    path("<str:page>/", menus, name="menus"),
]