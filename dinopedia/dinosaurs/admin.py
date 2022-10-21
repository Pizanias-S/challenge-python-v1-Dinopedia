from django.contrib import admin
from .models import Dino, Eating, Size, Period, Author, Comment

# Register your models here.


class DinoAdmin(admin.ModelAdmin):
    list_filter = ("name", "period", "size", "eating_class", "color", "author")
    list_display = ("name", "eating_class", "period", "size", "color", "author")
    prepopulated_fields = {"slug": ("name",)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post")


admin.site.register(Dino, DinoAdmin)
admin.site.register(Eating)
admin.site.register(Size)
admin.site.register(Period)
admin.site.register(Author)
admin.site.register(Comment, CommentAdmin)



