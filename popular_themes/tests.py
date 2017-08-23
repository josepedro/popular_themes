from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Theme

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
        self.assertEqual(theme_list[0].name, theme_1.name)
        self.assertEqual(theme_list[1].name, theme_2.name)
        self.assertContains(response, theme_1.name)
