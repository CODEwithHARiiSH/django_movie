from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import movie_forms
from .models import movies


# Create your views here.
def home(request):
    movie = movies.objects.all()
    context = {'movie_list': movie}

    return render(request, 'index.html', context)


def detail(request, movie_id):
    idd = movies.objects.get(id=movie_id)
    return render(request, 'details.html', {'idd': idd})


def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('name', )
        year = request.POST.get('year', )
        desc = request.POST.get('desc', )
        img = request.FILES['img']
        movie = movies(name=name, year=year, desc=desc, img=img)
        movie.save()
        return redirect('/')
    return render(request, 'add.html')


def update(request, id):
    idd = movies.objects.get(id=id)
    form = movie_forms(request.POST or None, request.FILES, instance=idd)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'idd': idd})

def delete(request,id):
    if request.method=='POST':
        mov=movies.objects.get(id=id)
        mov.delete()
        return redirect('/')
    return render(request,'delete.html')

