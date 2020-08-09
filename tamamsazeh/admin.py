from django.contrib import admin
from tamamsazeh.models import Article, Post,ProjectImage,Project


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    pass


class ProjectAdmin(admin.ModelAdmin):
    pass


class ProjectImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(ProjectImage, ProjectImageAdmin)
admin.site.register(Project, ProjectAdmin)
