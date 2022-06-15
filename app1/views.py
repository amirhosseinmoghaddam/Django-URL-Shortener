from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .generate_url import Generate_URL
from .models import Urls

def index(request):
    if request.method == "POST":
       new_path = Generate_URL()
       main_url = request.POST['main-url']   
       
       Urls(main_url= main_url, shorten_url= new_path).save()
       return render(request, 'index.html', {'shorten_url': new_path})

    else:
       return render(request, 'index.html')

def url(request, url):
    full_url = get_object_or_404(Urls ,shorten_url= url)
    return redirect(full_url.main_url)