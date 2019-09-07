from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views.generic import DetailView, FormView, ListView
from django.views.generic.base import View, TemplateView

from core.forms import UserForms, SidesForms
from core.models import Blog, Xiomi, News, Sides


def home(request):
    blog = Blog.objects.first()
    return HttpResponse(blog)


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
    page = request.GET.get('page', 1)

    paginator = Paginator(sides, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    last_sides = Sides.objects.last()
    embahome = Sides.objects.filter(created_at__lte=datetime.now())
    return render(request,'sides/sides_list.html',{'sides_list':users, 'last_sides': last_sides, 'embahome': embahome})

def sides_user(request):

    if request.POST:
        form = SidesForms(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.image = request.FILES['image']
            form.save()
            return HttpResponseRedirect(reverse('sides_upload'))
    else:
        form = SidesForms()

    return render(request, 'sides/sides_upload.html', {'form':form})


def sides_delete(request, sides_id):
    sides = Sides.objects.filter(id=int(sides_id)).last()
    if sides:
        sides.delete()
    return HttpResponseRedirect(reverse('sides_list'))

def sides_update(request, sides_id):
    sides_id = get_object_or_404(Sides, id=sides_id)
    form = SidesForms(request.POST or None, request.FILES or None, instance=sides_id)
    if form.is_valid() and request.POST:
        form.save(commit=False)
        if 'image' in request.FILES:
            form.image = request.FILES['image']
        form.save()
    return render(request, 'sides/sides_upload.html', {'form': form})


class DataJSONSender(View):
    pass

class Template(TemplateView):
    template_name = 'sides/sides_upload.html'


class Form(FormView):
    form_class = SidesForms()
    template_name = ''

class SidesList(ListView):
    template_name = 'sides/sides_list.html'
    model = Sides
    context_object_name = 'sides_list'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data()
        last_sides = Sides.objects.last()
        ctx['last_sides'] = last_sides
        return ctx

class SidesDetail(DetailView):
    template_name = 'sides/sides_det.html'
    model = Sides
    context_object_name = 'sides_det'


# def sides_det(request,sides_id):
#     sides_id = get_object_or_404(Sides, id=sides_id)
#     return render(request,'sides/sides_det.html',{'sides_det':sides_id})