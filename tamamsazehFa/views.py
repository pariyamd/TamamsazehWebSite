from django.shortcuts import render
from django.http import HttpResponse
from tamamsazehFa.models import ArticleFa,PostFa,ProjectFa

GENRE = ['نفت گاز و پتروشیمی','مراکز علمی آموزشی و فرهنگی',
         'سازه های فلزی و پلها',
         'ساختمانهای صنعتی و عمومی','انبوه سازی', 'راه سازی', 'دیگر پروژه ها']


def projects(request):
    return render(request=request, template_name='tamamsazehFa/projects.html',context={
        'projects': ProjectFa.objects.all()
    })


def main_page(request):
    return render(request=request, template_name='tamamsazehFa/main_page.html',context={
        'projects': ProjectFa.objects.all(),
        'genres': GENRE,
        'num':7
    })


def projectView(request,id):
    return render(request=request, template_name='tamamsazehFa/projectView.html',context={
        'project': ProjectFa.objects.all()[id]
    })


def base(request):
    return render(request=request, template_name='tamamsazehFa/base.html')


def certifications(request, num):
    return render(request=request, template_name='tamamsazehFa/certifications.html', context={"id": num})


def certificationsNon(request):
    return render(request=request, template_name='tamamsazehFa/certifications.html', context={"id": 1})


def aboutus(request):
    return render(request=request, template_name='tamamsazehFa/aboutus.html')


def crew(request):
    return render(request=request, template_name='tamamsazehFa/crew.html')


def article(request):
    return render(request=request, template_name='tamamsazehFa/article.html', context={
       'articles': ArticleFa.objects.all()
    })


def articleView(request,link):
    return render(request=request, template_name='tamamsazehFa/articleView.html', context={'link' : link})


def blog(request):
    return render(request=request, template_name='tamamsazehFa/blog.html', context={
        'posts': PostFa.objects.all()
    })

