from django.db import models
from .utils import unique_slug_generator,jcal,Shortner
from django.db.models.signals import pre_save
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
import random
from django.db.models import Q
import os
from django.utils import timezone
from django.utils.html import format_html
from django.core.files.storage import FileSystemStorage
from django.contrib.sites.shortcuts import get_current_site
from root import settings
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.CharField(max_length = 250,unique=True)
    lastname = models.CharField(max_length = 150 , blank=True)
    firstname = models.CharField(max_length = 150 , blank=True)
    profile_img = models.ImageField(upload_to='Users/Profile/' , blank=True)
    create_time = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    submit_email = models.BooleanField(default=False)
    
    objects = MyUserManager()
    #REQUIRED_FIELDS = ['lastname','firstname']
    USERNAME_FIELD = 'email'
    def __str__(self):
        return f"Email : {self.email} ID : {self.id}"

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    def fullname(self):
        name = self.lastname + self.firstname
        return name
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


templatefs = FileSystemStorage(location='cms/templates/page/')

# Create your models here.

class pwsrest(models.Model):
    email = models.CharField(max_length=150)
    uuid=models.CharField(max_length=250,unique=True)
    status = models.BooleanField(default=False)
    date = models.DateField(default=timezone.now) 
    time = models.TimeField(default=timezone.now)
    def __str__(self):
        return self.email
    class Meta:
        verbose_name = 'pwsrest'
        verbose_name_plural = 'pwsrest'

################################Blog model#############################








#####blog manager to customize queries
class BlogManager(models.Manager):
    ####search
    def search(self,q):
        lookup = Q(title__icontains=q) | Q(body__icontains=q) | Q(my_tags__title__icontains=q)
        if len(lookup) > 0:
            return self.get_queryset().filter(lookup,active=True).distinct()
        else:
            return None



    def active_Blogs(self):
        qs=self.get_queryset().filter(active=True)
        if qs.count() >= 1:
            return qs
        else:
            return None
    
    
    def get_by_slug(self,slug):
        qs=self.get_queryset().filter(active=True,slug=slug)
        if qs.count() == 1:
            return qs
        else:
            return None


######blog image url maker
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_name = random.randint(1, 27634723542)
    name, ext = get_filename_ext(filename)
    # final_name = f"{new_name}{ext}"
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"blog/{final_name}"




##################################blog tag model###########################################3
class Tag(models.Model):
    title=models.CharField(max_length=150)
    slug=models.SlugField(blank=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title





def tag_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(tag_save,sender=Tag)

################cat model#############################################
class Category(models.Model):
    title=models.CharField(max_length=150)
    slug=models.SlugField(blank=True)
    date=models.DateTimeField(auto_now_add=True)
    parent=models.ForeignKey('self',default=None,null=True,blank=True,on_delete=models.CASCADE,related_name='parents_cat')

    def __str__(self):
        return self.title

def category_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(category_save,sender=Category)




#################################################################################
########BLOG main model##########################################################################
#################################################################################
class Blog(models.Model):
    title=models.CharField(max_length=150,unique=True)
    slug=models.SlugField(blank=True, unique=True)
    body=RichTextUploadingField(blank=True,null=True)
    image=models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    active=models.BooleanField(default=False)
    publish_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    publisher = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    my_tags = models.ManyToManyField(Tag, blank=True)
    category = models.ManyToManyField(Category, blank=True)
    star=models.ManyToManyField(User,blank=True,related_name="like_star")
    seen=models.IntegerField(blank=True,null=True,default=0)
    short_link=models.CharField(max_length=20,null=True,blank=True)



    objects=BlogManager()
    def __str__(self):
        return self.title


    def number_of_starts(self):
        return self.star.count()
    def thumbnail_tag(self):

        return format_html("<img width=30 height=30 style='border-radius: 5px;' src='{}'>".format(self.image.url))
		

    def jcal_time(self):
        return jcal(self.publish_time)
    jcal_time.short_description = "published time"

    def long_link(self):
        return settings.MY_HOST+"blog/"+self.slug
    def short_link_def(self):
        return settings.MY_HOST+"sl/show/"+self.short_link

####Blog slug creator###
def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Blog)




#######################Comment sys#############################
######################
#####################

####MAin comment##################

class CommentBlog(models.Model):
    sender=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    text= models.TextField()
    posted_time = models.DateTimeField(auto_now_add=True, editable=False)
    blog= models.ForeignKey(Blog, on_delete=models.CASCADE,related_name='comments')
    active=models.BooleanField(default=False)
    like=models.ManyToManyField(User,blank=True,related_name="like_comment")
    dislike=models.ManyToManyField(User,blank=True,related_name="dislike_comment")

    
    def number_of_likes(self):
        return self.like.count()
    def number_of_dislikes(self):
        return self.dislike.count()
    ########################################################################################


    ########################ticket sys ##################################
    #######################
    ####################

        
class templatedir(models.Model):
    token = models.CharField(unique=True,max_length=250)
    file = models.FileField(storage=templatefs)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.token
    class Meta:
        verbose_name = 'templatedir'
        verbose_name_plural = 'templatedirs'


class menu(models.Model):
    name = models.CharField(max_length = 150)
    link = models.CharField(max_length = 250,blank=True)
    file = models.ManyToManyField(templatedir,blank=True,related_name='file_template')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'menu'
        verbose_name_plural = 'menus'




class chanel(models.Model):
    token = models.UUIDField(unique=True)
    createor = models.ManyToManyField(User,related_name="createor")
    date  = models.DateTimeField(auto_now_add=True)
    vazit = models.BooleanField(default=False)
    title = models.CharField(max_length=250,blank=True)

    def jcal_time(self):
        return jcal(self.date)
    class Meta:
        verbose_name = 'chanel'
        verbose_name_plural = 'chanels'

class ticket(models.Model):
    chanel = models.ForeignKey(chanel,on_delete=models.CASCADE)
    sender = models.CharField(max_length = 150)
    title = models.CharField(max_length = 250,blank=True,null=True)
    mozoee = models.CharField(max_length = 250,blank=True,null=True)
    des = models.TextField()
    date  = models.DateTimeField(default=timezone.now,blank=True)
    def jcal_time(self):
        return jcal(self.date)
    class Meta:
        verbose_name = 'ticket'
        verbose_name_plural = 'tickets'




#################blog short link #######################
#################
class ShortUrls(models.Model):
    short=models.CharField(max_length = 20,unique=True)
    long=models.URLField("URL",unique=True)
    

    ########short pre save blog

    
    
def sl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.short_link:
        instance.short_link = Shortner().issue_token()
        ShortUrls.objects.create(long=instance.long_link(),short=instance.short_link)


pre_save.connect(sl_pre_save_receiver, sender=Blog)