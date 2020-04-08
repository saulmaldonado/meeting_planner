from django.shortcuts import render, get_object_or_404, redirect

from .models import Meeting, Room
from .forms import MeetingForm


def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id) # get_object_or_404 will return the object with the given id or a 404 error
    return render(request, 'meetings/detail.html', {'meeting': meeting})

def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'meetings/rooms.html', {'rooms': rooms})



def new(request):

    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        form = MeetingForm()

    return render(request, 'meetings/new.html',{'form': form} )