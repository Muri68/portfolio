from django.contrib import admin
from .models import Project, ProjectInMind, Contact, Category


class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'subject', 'message', 'reply')
    list_editable = ('reply',)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }



class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_title', 'category', 'date_posted')
    prepopulated_fields = {'slug': ('project_title',), }
    list_filter = ('category',)
    list_per_page = 5
    search_fields = ('project_title',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectInMind)
admin.site.register(Contact, ContactAdmin)