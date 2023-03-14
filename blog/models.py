from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.db import models
from django.template.defaultfilters import slugify

User = get_user_model()


class Categorie(models.Model):
    nom = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def __str__(self):
        return self.nom


class Article(models.Model):
    titre = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    derniere_mise_a_jour = models.DateTimeField(auto_now=True)
    date_de_creation = models.DateField(blank=True, null=True)
    contenu = models.TextField(blank=True, verbose_name="Contenu")
    auteur = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    categories = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True, blank=True)
    images = models.ImageField(blank=True, upload_to='imagesblog')

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)

        super().save(*args, **kwargs)


class Commentaire(models.Model):
    date_de_publication = models.DateTimeField(auto_now_add=True)
    nom_lecteur = models.CharField(max_length=255, null=True, blank=True)
    email_lecteur = models.EmailField(max_length=255, null=True, blank=True)
    contenu = models.TextField(verbose_name="Contenu")
    auteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auteur', null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='commentaire')

    def __str__(self):
        return self.contenu
