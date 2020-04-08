from django.shortcuts import render, get_object_or_404

from .models import Meeting, Room


def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id) # get_object_or_404 will return the object with the given id or a 404 error
    return render(request, 'meetings/detail.html', {'meeting': meeting})

def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'meetings/rooms.html', {'rooms': rooms})