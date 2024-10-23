from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .rockadd_form import RockAddForm
from ..models import Lake

from icecream import ic


# @login_required
def rockadd(request, **kwargs):
    context = {}

    if 'lakeslug' in kwargs:
        lakeslug = kwargs['lakeslug']
        try:
            lake = Lake.objects.get(slug=lakeslug)
            rock_form = RockAddForm(lake_id=lake.id)
            rock_form.fields['lake'].initial = lake
            context['lake'] = lake
        except Lake.DoesNotExist:
            messages.error(request, 'Lake not found: ' + lakeslug)
            # redirect user

    if request.method == 'POST':
        rock_form = RockAddForm(request.POST)
        if rock_form.is_valid():
            rock_form.save()
            messages.success(request, 'Your Rock was successfully added' + lake.name)
        else:
            messages.error(request, ('Error Saving Rock', rock_form.errors))

        return redirect('rockadd_by_lake', lakeslug=lakeslug)
 
    context['form'] = rock_form

    return render(request, 'rocks/rockadd.html', context)
