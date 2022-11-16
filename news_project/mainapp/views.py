from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from mainapp.forms import CommentForm, MailForm

from mainapp.models import News, Comments, Favorite

from news_project import settings


def index(request):
    news = News.objects.all()
    paginate = Paginator(news, 1)
    print(paginate)
    page_number = request.GET.get('page')
    page_object = paginate.get_page(page_number)
    context = {
        'news': page_object,
    }
    return render(request, 'mainapp/index.html', context)


def select_news(request, pk):
    news = get_object_or_404(News, id=pk)
    comment = Comments.objects.filter(news=news, status=Comments.Status.FIRST)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid:
            form_2 = form.save(commit=False)
            form_2.user = request.user
            form_2.news = news
            form_2.save()
            return HttpResponseRedirect(reverse('mainapp:select_news', kwargs={'pk': news.id}))
    else:
        form = CommentForm

    context = {
        'title': news.title,
        'news': news,
        'comments': comment,
        'form': form,
    }
    return render(request, 'mainapp/select_news.html', context)


def comments(request):
    comment = Comments.objects.all()
    context = {
        'title': 'главная',
        'comment': comment
    }
    return render(request, 'mainapp/comment.html', context)


def create_comments(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mainapp:comment'))
    else:
        form = CommentForm()
    context = {
        'title': 'добавить комментарий',
        'form': form,
    }
    return render(request, 'mainapp/add/comment.html', context)


def remove_comments(request, pk):
    comment = get_object_or_404(Comments, id=pk)
    comment.delete()
    return HttpResponseRedirect(reverse('mainapp:comment'))


def update_comments(request, pk):
    comment = get_object_or_404(Comments, id=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mainapp:comment'))
    else:
        form = CommentForm(instance=comment)

    context = {
        'title': 'добавить комментарий',
        'form': form,
    }
    return render(request, 'mainapp/edit/comment.html', context)


def about(request):
    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            message = f'От: {form2.email}, Тема: {form2.theme} \nТекст: {form2.text}\n'
            send_mail(form2.theme, message, settings.EMAIL_HOST_USER, ['crimecrew21@mail.ru'])
            if send_mail:
                form2.save()
                return HttpResponseRedirect(reverse('mainapp:about'))
    else:
        form = MailForm()
    context = {
        'title': 'братная связь',
        'form': form,
    }
    return render(request, 'mainapp/about.html', context)


def favorite(request):
    favor = Favorite.objects.filter(user=request.user)
    context = {
        'title': 'избранное',
        'favorite': favor,
    }
    return render(request, 'mainapp/favorite.html', context)

def add_favorite(request, pk):
    news = get_object_or_404(News, id=pk)
    Favorite.objects.get_or_create(
        news=news,
        user=request.user
    )
    return  HttpResponseRedirect(reverse('mainapp:index'))
def remove_favorite(request, pk):
    favor = get_object_or_404(Favorite, id=pk)
    favor.delete()
    return HttpResponseRedirect(reverse('mainapp:index'))