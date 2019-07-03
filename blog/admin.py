from django.contrib import admin
from .models import Post, Comment
from django.utils.safestring import mark_safe

#admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo_tag')

    def photo_tag(self, post):
        #return '<img src="{}" />'.format(post.photo.url)
        return mark_safe('<img src="{}" style="width: 100px;" />'.format(post.photo.url))
    photo_tag.allow_tags = True

admin.site.register(Comment)



# Register your models here.
