from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .forms import RockForm
from django.contrib.auth.decorators import login_required

@login_required
def addrock(request):
    if request.method == 'POST':
        rock_form = RockForm(request.POST)
        if rock_form.is_valid():
            rock_form.save()
            messages.success(request, 'Your Rock was successfully added!')
        else:
            messages.error(request, ('Error saving Rock', rock_form.errors))
        return redirect('addrock')
    rock_form = RockForm()
    return render(request, 'rocks/addrock.html', {'form': rock_form})
    # return HttpResponse("Track Rocks Here.")
