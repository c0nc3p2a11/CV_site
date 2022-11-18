from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    template = 'main/index.html'
    # posts = Post.objects.order_by('-pub_date')[:10]
    # title = 'Это главная страница проекта Yatube'
    # text = 'Последние обновления на сайте'
    # context = {
    #     'posts': posts,
    #     'title' : title,
    #     'text': text
    # }
    # return render(request, template, context)
