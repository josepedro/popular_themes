from django.test import TestCase
from django.core.urlresolvers import reverse
from datetime import datetime

from .models import Theme
from .models import Video
from .models import Comment
from .models import Thumb

class ThemeIndexViewTests(TestCase):
    
    def test_no_themes(self):
        # If no themes exist, an appropriate message is displayed.
        response = self.client.get(reverse('popular_themes:get_popular_themes'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No themes are available.")
        self.assertQuerysetEqual(response.context['sorted_theme_list'], [])

    def test_list_themes(self):
    	# Check if accounts appear
        theme_1 = Theme.objects.create(name='test_1')
        theme_2 = Theme.objects.create(name='test_2')
        response = self.client.get(reverse('popular_themes:get_popular_themes'))
        theme_list = response.context['sorted_theme_list']
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, theme_1.name)

    def test_list_sorted_themes(self):
        # Check if accounts appear
        date = datetime.now
        theme_1 = Theme.objects.create(name='test_1')
        theme_2 = Theme.objects.create(name='test_2')
        video_1 = Video.objects.create(name='video_1', views=5, date_uploaded=date)
        video_1.themes.add(theme_2)
        video_2 = Video.objects.create(name='video_2', views=10, date_uploaded=date)
        video_2.themes.add(theme_1)
        video_2.themes.add(theme_2)
        thumb_1 = Thumb.objects.create(is_positive=False, video=video_1, time=date)
        thumb_2 = Thumb.objects.create(is_positive=True, video=video_2, time=date)
        comment_1 = Comment.objects.create(is_positive=True, video=video_1, time=date)
        comment_2 = Comment.objects.create(is_positive=True, video=video_2, time=date)

        response = self.client.get(reverse('popular_themes:get_popular_themes'))
        theme_list = response.context['sorted_theme_list']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(theme_list[0].name, theme_2.name)
        self.assertEqual(theme_list[1].name, theme_1.name)
        self.assertContains(response, theme_2.name)
