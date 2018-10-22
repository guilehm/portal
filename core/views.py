from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.utils import timezone


@login_required
def index(request):
    now = timezone.now()
    return render(request, 'core/index.html', {
        'now': now,
    })


def logout_view(request):
    logout(request)
    return redirect('core:index')


def login_view(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    if request.method != 'POST':
        form = AuthenticationForm()
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            authenticated_user = authenticate(
                username=request.POST['username'],
                password=request.POST['password']
            )
            login(request, authenticated_user)
            return redirect('core:index')
    return render(request, 'core/login.html', {
        'form': form,
        'ip': ip,
    })
