from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable":"my name is darpan",
        "name":'darpan'
    }
    return render(request, 'index.html', context)

def about(request):
    return HttpResponse("This is a about")

def contact(request):
    return HttpResponse("This is a Contact page")