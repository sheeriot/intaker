from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .rockeditrow_form import RockEditRowForm
from ..models import Lake, Rock

from icecream import ic


@login_required
def rockstable_edit(request, **kwargs):
    # form = RockEditRowForm()
    context = {}

    if 'lakeslug' in kwargs:
        lakeslug = kwargs['lakeslug']
        try:
            lake = Lake.objects.get(slug=lakeslug)
            context['lake'] = lake
            rocks = Rock.objects.filter(lake=lake)
            context['rocks'] = rocks
            rock_forms = {rock.id: RockEditRowForm(instance=rock) for rock in rocks}
            context['rock_forms'] = rock_forms
            return render(request, 'rocks/rocksedit.html', context)

        except Lake.DoesNotExist:
            messages.error(request, 'Lake not found: ' + lakeslug)
            # redirect user
            return redirect('lakes')

    # if request.method == 'POST':
    #     rock_form = RockAddForm(request.POST)
    #     if rock_form.is_valid():
    #         rock_form.save()
    #         messages.success(request, 'Your Rock was successfully added' + lake.name)
    #     else:
    #         messages.error(request, ('Error Saving Rock', rock_form.errors))

    #     return redirect('rockadd_by_lake', lakeslug=lakeslug)

