from django.shortcuts import render

# Create your views here.

def preferences_home(request):
    return render(
        request,
        'preferences/home.html',
        {

        }
    )
