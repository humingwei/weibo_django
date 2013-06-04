from django.contrib import admin
from models import Cal

class CalAdmin(admin.ModelAdmin):
    date_hierarchy = 'time'
    list_filter = ('username',)
    search_fields = ('username', 'x')
    list_display = ('username', 'x', 'y', 'sum', 'time')

    def sum(self, obj):
        return obj.sum()
    sum.short_descripition = "Sum"

admin.site.register(Cal, CalAdmin)
