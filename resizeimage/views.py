from django.shortcuts import render
from .models import ImageResize
from .utils import Resizer2

# Create your views here.

def home(request):
    if request.method=='POST':
        image = request.FILES.get('image')
        laje = request.POST.get('laje')
        ote = request.POST.get('ote')
        img=ImageResize(imagesubmit=image,width=laje,heigth=ote)
        img.save()
        #Resizer(img.imagesubmit,laje,ote)
        ima=Resizer2(img.imagesubmit,int(laje),int(ote))
        img.imageresize=ima
        img.save()
        print(image)
        print(int(laje)+2)
        print(int(ote)+2)
    return render(request,'index.html')

def ri(request):

    l=ImageResize.objects.all()

    context={
        'l':l,
    }
    return render(request,'image.html',context)