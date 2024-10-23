from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.contrib import messages
from django.contrib.auth.decorators import login_required

# from .forms import RockForm
from ..models import Lake

from icecream import ic


@login_required
def lakes(request, **kwargs):
    # start with a blank context
    context = {}

    # Get all Lake objects
    lakes = Lake.objects.all()
    # Count rocks per lake and add to the lakes list
    for lake in lakes:
        lake.rock_count = lake.rocks.count()
    
    # Add the lakes to the context
    context['lakes'] = lakes
    
    # Render the template with the context
    return render(request, 'rocks/lakes.html', context)
