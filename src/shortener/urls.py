from django.urls import path

from .views import IndexView, ShowShortUrlView, RedirectUrlView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('show/<slug:shortcode>/', ShowShortUrlView.as_view(), name='show-shorturl'),
    path('<slug:shortcode>/', RedirectUrlView.as_view(), name='redirect')
]