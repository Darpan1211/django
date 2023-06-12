from django.shortcuts import render
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
     return render(request, 'index.html')
    
def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        city = request.POST.get('city')
        contact = Contact(name=name, email=email, city=city, date = datetime.today())
        contact.save()
        messages.success(request, "Your Message has been sent.")

    return render(request, 'contact.html')

def service(request):
      return render(request, 'service.html')