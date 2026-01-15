from django.shortcuts import render
from .models import Student

# Create your views here.
def home(req):
    return render(req,"home.html")

def frormdata(req):
   if req.method=='POST':
       n = req.POST.get('username')
       p = req.POST.get('password')
       photu = req.FILES.get('profile_pic')
       document = req.FILES.get('document')
   print(n,p,photu,document)
#    print(q.getlist)
   Student.objects.create(name=n,password=p,photo=photu,document=document)


