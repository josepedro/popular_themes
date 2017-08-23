from django.conf.urls import url
from . import views

app_name = 'popular_themes'
urlpatterns = [
    url(r'^$', views.get_popular_themes, name='get_popular_themes'),
]