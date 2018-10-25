from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.cache import cache
from django.shortcuts import redirect, render
from django.utils import timezone

from utils.weather import get_weather_data


@login_required
def index(request):
    now = timezone.now()
    context = {'now': now}
    woeid = request.user.woeid or 455863
    has_data = cache.get(str(woeid))
    if not has_data:
        data = get_weather_data(woeid)
        context.update(data) if data else context
    else:
        context.update(has_data)
    return render(request, 'core/index.html', context)


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
