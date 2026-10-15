from django.shortcuts import render

def landing(request):
    return render(request, 'home/landing.html')

# def home(request):
#     return render(request, 'home/home.html')


def home(request):
    context = {
        'title': 'Fernand Home Page',
        'message': 'Welcome to my first Django application!'
    }

    return render(
        request,
        'home/home.html',
        context
    )
