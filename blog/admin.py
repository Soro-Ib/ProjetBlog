from django.contrib import admin

from blog.models import Article, Commentaire, Categorie

# Register your models here.
admin.site.register(Article)
admin.site.register(Categorie)
admin.site.register(Commentaire)
