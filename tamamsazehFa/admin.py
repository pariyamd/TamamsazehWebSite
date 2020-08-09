
from django.contrib import admin

from tamamsazehFa.models import ArticleFa, PostFa,ProjectFa


# Register your models here.


class ArticleFaAdmin(admin.ModelAdmin):
    pass


class PostFaAdmin(admin.ModelAdmin):
    pass


class ProjectFaAdmin(admin.ModelAdmin):
    pass


class ProjectImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(PostFa, PostFaAdmin)
admin.site.register(ArticleFa, ArticleFaAdmin)
admin.site.register(ProjectFa, ProjectFaAdmin)
