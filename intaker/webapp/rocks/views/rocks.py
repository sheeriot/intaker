from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.contrib import messages
from django.contrib.auth.decorators import login_required

# from .forms import RockForm
from ..models import Lake, Rock

from icecream import ic


@login_required
def rocks(request, **kwargs):
    # start with a blank context
    context = {}
    # Get the lake_id from the GET request if it exists
    lakeslug = request.GET.get('lakeslug')

    # ic(kwargs)
    if not lakeslug:
        lakeslug = kwargs.get('lakeslug')

    if lakeslug:
        try:
            lake = Lake.objects.get(slug=lakeslug)
            rocks = Rock.objects.filter(lake=lake)
            context['rocks'] = rocks
            context['lake'] = lake
        except Lake.DoesNotExist:
            context['lake'] = None
            context['rocks'] = Rock.objects.none()
    
    # Render the template with the context
    return render(request, 'rocks/rocklist.html', context)
