from django.shortcuts import render
from visitka.models import Service, Main

# Create your views here.

def index(request):
    main = Main.objects.all()
    context = {
        'main': main
    }
    print(main)
    return render(request, 'index.html', context=context)

def about(request):
    return render(request, 'about.html')

def services(request):
    services = Service.objects.all()
    context = {
        'services': services
    }
    return render(request, 'services.html', context=context)

def contacts(request):
    return render(request, 'contacts.html')
