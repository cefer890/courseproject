from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views.generic import DetailView

from core.forms import UserForms, SidesForms
from core.models import Blog, Xiomi, News, Sides


def home(request):
    blog = Blog.objects.first()
    return HttpResponse(blog.desc)


def xiomi(request):
    xiomi = Xiomi.objects.all()[:8]
    news  = News.objects.all()[:8]
    return render(request,'xiomi/xiomi_list.html',{'xiomi_det':xiomi, 'news': news})

def xiomi_det(request,xiomi_id):
    xiom_id = Xiomi.objects.get(id=xiomi_id)
    xiom_id.view_count+=1
    xiom_id.save()
    return render(request,'xiomi/xiomi_det.html',{'xiomi_det':xiom_id})

def news_det(request, news_id):
    news_id = News.objects.get(id=news_id)
    return render(request, 'xiomi/xiomi_det.html', {'xiomi_det': news_id})


def reg_user(request):
    form = UserForms(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'users/reg.html', {'form':form})

from datetime import datetime

def sides(request):
    sides = Sides.objects.all()
    last_sides = Sides.objects.last()
    embahome = Sides.objects.filter(created_at__lte=datetime.now())
    return render(request,'sides/sides_list.html',{'sides_list':sides, 'last_sides': last_sides, 'embahome': embahome})

def sides_det(request,sides_id):
    sides_id = get_object_or_404(Sides, id=sides_id)
    return render(request,'sides/sides_det.html',{'sides_det':sides_id})

def sides_user(request):

    if request.POST:
        form = SidesForms(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.image = request.FILES['image']
            form.save()
    else:
        form = SidesForms()

    return render(request, 'sides/sides_upload.html', {'form':form})


def sides_delete(request, sides_id):
    sides = Sides.objects.filter(id=int(sides_id)).last()
    if sides:
        sides.delete()
    return HttpResponseRedirect(reverse('sides_list'))


