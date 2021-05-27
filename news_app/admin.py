from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, News


class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'category',
        'created_at',
        'updated_at',
        'is_published',
        'views',
        'get_photo'
    )
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    fields = (
        'title',
        'category',
        'content',
        'photo',
        'get_photo',
        'is_published',
        'views',
        'created_at',
        'updated_at',
    )
    readonly_fields = ('get_photo', 'views', 'created_at', 'updated_at')
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}", width="270">')
        else:
            return '-'

    # We set here a name for 'list_display'
    get_photo.short_description = 'Image'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'News Management'
admin.site.site_header = 'News Management'
