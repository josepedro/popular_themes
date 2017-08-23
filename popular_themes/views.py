from django.shortcuts import render

from .models import Theme

def get_popular_themes(request):

        

    sorted_theme_list = Theme.objects.all()
    context = {'sorted_theme_list': sorted_theme_list}
    return render(request, 'popular_themes/index.html', context)
