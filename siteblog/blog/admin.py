from django.contrib import admin

from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    form = PostAdminForm
    save_on_top = True
    list_display = ('id', 'title', 'slug', 'category', 'created_at', 'get_photo', 'fixed',)
    list_display_links = ('id', 'title',)
    search_fields = ('title',)
    list_filter = ('category', 'tags', 'fixed',)
    readonly_fields = ('views', 'created_at', 'get_photo',)
    fields = ('title', 'slug', 'category', 'tags', 'content', 'author', 'get_photo', 'photo', 'views', 'created_at', 'fixed',)

    def get_photo(self, odj):
        if odj.photo:
            return mark_safe(f'<img src="{odj.photo.url}" width=50>')
        return '-'

    get_photo.short_description = 'Photo'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title',)


@admin.register(MainSlider)
class MainSliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_photo')
    list_display_links = ('id', 'title',)
    readonly_fields = ('created_at', 'get_photo',)
    fields = ('title', 'content', 'get_photo', 'photo', 'created_at',)

    def get_photo(self, odj):
        if odj.photo:
            return mark_safe(f'<img src="{odj.photo.url}" width=50>')
        return '-'

@admin.register(EmailSubscriptions)
class EmailSubscriptionsAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at',)
    save_on_top = True
