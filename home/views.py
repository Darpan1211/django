from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable':"This is text"
    }
    return render(request, 'index.html', context)

def about(request):
    return HttpResponse("This is a about")