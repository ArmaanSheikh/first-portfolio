from django.shortcuts import render,get_object_or_404
from blog.models import BlogProject
# Create your views here.

def index(request):
    blog = BlogProject.objects.order_by('-date')
    return render(request,'blog/blogindex.html',{'blog':blog})

def details(request,blog_id):
    blog = get_object_or_404(BlogProject, pk=blog_id)
    return render(request,'blog/details.html',{'blog':blog})
