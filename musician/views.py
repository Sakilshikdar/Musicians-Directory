from django.shortcuts import render
from musician.models import  MusicianForm

# Create your views here.

def musicianhome(request):


    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect or do something upon successful form submission
    else:
        form = MusicianForm()
    return render(request, "musicianHome.html", {'form':form})

