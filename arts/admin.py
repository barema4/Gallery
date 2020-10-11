from django.contrib import admin
from .models import Picture, Review


class ReviewInline(admin.TabularInline):

    model = Review

class PictureAdmin(admin.ModelAdmin):

    inlines = [
          ReviewInline,
        ]
    list_display = ("title", "author", "price",)

admin.site.register(Picture,PictureAdmin)