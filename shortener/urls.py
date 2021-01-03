from django.urls import path

from .views import IndexView, ShowShortUrlView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('show/<slug:shortcode>/', ShowShortUrlView.as_view(), name='show-shorturl')
]