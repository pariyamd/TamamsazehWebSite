from django.shortcuts import render
from django.http import HttpResponse
from tamamsazeh.models import Article,Post,Project

GENRE = ['Oil, Gas and Petrochemical','Educational and Cultural Structures',
         'Steal Structures and Bridges',
         'Industrial and Civil Structure','Mass production', 'Road construction', 'Others']


def projects(request):
    return render(request=request, template_name='tamamsazeh/projects.html',context={
        'projects': Project.objects.all()
    })


def projectView(request,id):
    return render(request=request, template_name='tamamsazeh/projectView.html',context={
        'projects': Project.objects.all(),
        'num_id':id
    })


def main_page(request):
    return render(request=request, template_name='tamamsazeh/main_page.html',context={
        'projects': Project.objects.all(),
        'genres': GENRE,
        'num':7
    })


def base(request):
    return render(request=request, template_name='tamamsazeh/base.html')


def certifications(request, num):
    return render(request=request, template_name='tamamsazeh/certifications.html', context={"id": num})


def certificationsNon(request):
    return render(request=request, template_name='tamamsazeh/certifications.html', context={"id": 1})


def aboutus(request):
    return render(request=request, template_name='tamamsazeh/aboutus.html')


def crew(request):
    return render(request=request, template_name='tamamsazeh/crew.html')


def article(request):
    return render(request=request, template_name='tamamsazeh/article.html', context={
       'articles': Article.objects.all()
    })


def articleView(request,link):
    return render(request=request, template_name='tamamsazeh/articleView.html', context={'link' : link})


def blog(request):
    return render(request=request, template_name='tamamsazeh/blog.html', context={
        'posts': Post.objects.all()
    })

