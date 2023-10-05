from django.contrib import admin
from newPosts.models import newPost

class blogPost(admin.ModelAdmin):
    list_display = ('title','titleSlug','description','postImg')


admin.site.register(newPost,blogPost)

# Register your models here.
