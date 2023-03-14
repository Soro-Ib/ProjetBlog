from django.forms import ModelForm
from .models import Commentaire


class CommentaireForm(ModelForm):
    class Meta:
        model = Commentaire
        fields = ['nom_lecteur', 'email_lecteur', 'contenu']
