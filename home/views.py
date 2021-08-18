from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
# Create your views here.
def index(request):
    context = {
        'variable':"this is sent",
        'variable2':"this is v2"
    }
    return render(request, 'index.html', context)
   
def aboutpage(request):
    return render(request, 'aboutpage.html')
def contact(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()

    return render(request, 'contact.html')
def services(request):
    return render(request, 'services.html')
def login(request):
    return render(request, 'login.html')
def wallpapers(request):
    return render(request, 'wallpapers.html')
def blog(request):
    return render(request, 'blog.html')
def movies(request):
    return render(request, 'movies.html')
def faq(request):
    return render(request, 'faq.html')
def ourstory(request):
    return render(request, 'ourstory.html')
def products(request):
    return render(request, 'products.html')
def recipies(request):
    return render(request, 'recipies.html')
    