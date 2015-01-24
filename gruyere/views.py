from django.contrib.auth.decorators import login_required
from django.db import connection
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import LoginForm


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            cursor = connection.cursor()
            query = "SELECT COUNT(*) FROM auth_user WHERE username = '%s' AND password = '%s'" % \
                    (username, password)
            cursor.execute(query)
            result = cursor.fetchone()[0]
            if result:
                return HttpResponseRedirect('/main/')
            return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'index.html', {'form': form})


@login_required(login_url='/')
def main(request):
    return HttpResponse('We\'re in the main page!')
