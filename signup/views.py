from django.shortcuts import render,redirect,get_object_or_404
from .models import Signup
# Create your views here.

def home(request):
   signups = Signup.objects.all()
   return render(request, 'home.html', {'signups':signups})

def detail(request,id):
    signup = get_object_or_404(Signup, pk = id)
    return render(request,'detail.html',{'signup':signup})

def new(request):
    return render(request,'new.html')

def create(request):
    new_signup = Signup()
    new_signup.name = request.POST['name']
    new_signup.age = request.POST['age']
    new_signup.pub_date = request.POST['pub_date']
    new_signup.email = request.POST['email']
    new_signup.introduce = request.POST['introduce']
    new_signup.save()
    return redirect('detail',new_signup.id)