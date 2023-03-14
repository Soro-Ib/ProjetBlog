from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from blog.form import CommentaireForm
from blog.models import Article, Categorie, Commentaire


# Create your views here.
def home(request):
    articles = Article.objects.all()
    categories = Categorie.objects.all()
    return render(request, 'blog/home.html', context={'articles': articles, 'categories': categories})


def detail_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            new_commentaire = form.save(commit=False)
            new_commentaire.article = article
            new_commentaire.auteur = request.user if request.user.is_authenticated else None
            new_commentaire.save()
            return HttpResponseRedirect(reverse('detail_article', args=[article.slug]))
    else:
        form = CommentaireForm()
    return render(request, 'blog/article_detail.html', context={'article': article, 'form': form})


def modifier_comment(request, id):
    commentaire = get_object_or_404(Commentaire, id=id)
    form = CommentaireForm(request.POST or None, instance=commentaire)
    if form.is_valid():
        form.save()
        return redirect('detail_article', slug=commentaire.article.slug)
    return render(request, 'blog/modifer_commentaire.html', {'form': form})


@login_required
def supprimer_comment(request, id):
    commentaire = get_object_or_404(Commentaire, id=id)
    article = commentaire.article.slug
    commentaire.delete()
    return redirect('detail_article', slug=article)
