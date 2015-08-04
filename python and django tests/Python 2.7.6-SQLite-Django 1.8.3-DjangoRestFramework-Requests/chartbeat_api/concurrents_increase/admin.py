from django.contrib import admin
from concurrents_increase.models import Domain, Page
# Register your models here.


class PageAdmin(admin.ModelAdmin):
    list_display = ('i', 'path', 'domain_id')


admin.site.register(Domain)
admin.site.register(Page, PageAdmin)