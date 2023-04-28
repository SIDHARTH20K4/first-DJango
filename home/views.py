from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context = {'variable' : 'sid is great'}
    return render(request,'index.html',context)

def about(request):
    return HttpResponse('this is about page')

def services(request):
    return HttpResponse('this is services page')

def contact(request):
    return render(request,'contact.html')
