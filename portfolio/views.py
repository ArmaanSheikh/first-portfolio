from django.shortcuts import render
from portfolio.models import ProtforlioProject
# Create your views here.
def index(request):
    portfolio_project = ProtforlioProject.objects.all()
    return render(request,'portfolio/index.html',{'portfolio_project':portfolio_project})
