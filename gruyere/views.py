from django.contrib.auth.decorators import login_required
from django.db import connection
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import LoginForm


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            if result:
                return HttpResponseRedirect('/main/')
            return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'index.html', {'form': form})


@login_required(login_url='/')
def main(request):
    return HttpResponse('We\'re in the main page!')
