from django.contrib import admin
from bksystem.models import books
# Register your models here.

class booksAdmin(admin.ModelAdmin):
    list_display=['id','title','author','isbn','publisher','publication_year','last_modified_date','created_date','created_at','update_at']

admin.site.register(books,booksAdmin)