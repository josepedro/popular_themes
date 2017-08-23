from django.shortcuts import render
from datetime import datetime
from django.utils import timezone

from .models import Theme
from .models import Video
from .models import Comment
from .models import Thumb

def sort_themes_by_score():
    # calculate score videos
    videos_list = Video.objects.all()
    scores_themes = dict()
    for theme in Theme.objects.all():
        scores_themes[theme.id] = 0
    year_now = timezone.now().year
    date_time_reference = timezone.now()
    for video in videos_list:
        date_since_upload = date_time_reference - video.date_uploaded
        days_since_upload = date_since_upload.days
        time_factor = max(0, 1 - (days_since_upload/365))
        views = video.views
        comments = Comment.objects.filter(video=video)
        good_comments = 0
        if len(comments) != 0:
            positive_comments = len([comment for comment in comments if comment.is_positive == True])
            negative_comments = len([comment for comment in comments if comment.is_positive == False])
            good_comments = positive_comments/(positive_comments+negative_comments)
        thumbs = Thumb.objects.filter(video=video)
        thumbs_up = 0
        if len(thumbs) != 0:
            thumbs_up = len([thumb for thumb in thumbs if thumb.is_positive == True])
            thumbs_down = len([thumb for thumb in thumbs if thumb.is_positive == False])
            thumbs_up = thumbs_up/(thumbs_up+thumbs_down)
        positivity_factor = 0.7 * good_comments + 0.3 * thumbs_up
        score = views*time_factor*positivity_factor 
        themes = video.themes.all()
        for theme in themes:
            scores_themes[theme.id] += score
    return sorted(Theme.objects.all(), key=lambda theme: scores_themes[theme.id], reverse=True)

def get_popular_themes(request):
    sorted_theme_list = sort_themes_by_score()
    context = {'sorted_theme_list': sorted_theme_list}
    return render(request, 'popular_themes/index.html', context)
