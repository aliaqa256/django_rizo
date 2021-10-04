from django.contrib import admin

from cms.models import *

from .models import Blog,Tag,Category

class BlogAdmin(admin.ModelAdmin):
	list_display = ('title', 'thumbnail_tag','active','publisher','jcal_time')
	list_filter = ('active','publisher', 'created_time')
	search_fields = ('title','body')
	prepopulated_fields = {'slug': ('title',)}
	ordering = ['-created_time']

# admin.site.register(Blog)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(pwsrest)
admin.site.register(Blog,BlogAdmin)
admin.site.site_header="Action CMS"
admin.site.register(CommentBlog)
admin.site.register(templatedir)
admin.site.register(menu)
admin.site.register(chanel)
admin.site.register(ticket)
admin.site.register(ShortUrls)


# Register your models here.




