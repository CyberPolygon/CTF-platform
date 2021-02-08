from django.shortcuts import render

# Create your views here.


def show_event_list(request, platform_name):
    """
    Рендеринг главной страницы с событиями
    """
    return render(request, f'{platform_name}/index.html')


def show_event(request, platform_name, event_id):
    """
    Рендериг страницы с конкретным событием
    """
    return render(request, f'{platform_name}/index.html')
