from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post

def ciao(request):
    return HttpResponse("ciao")


def index(request):
     object_list = Post.objects.all()
     return render(request, "blog/index.html", {
         'object_list': object_list})