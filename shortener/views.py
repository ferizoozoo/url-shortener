from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView, RedirectView

from .models import ShortenedUrl
from .forms import ShortenUrlForm

# Create your views here.
class IndexView(FormView):
    template_name = 'shortener/index.html'
    form_class = ShortenUrlForm
    success_url = ''

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ShowShortUrlView(TemplateView):
    template_name = 'shortener/shorturl.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        shortcode = kwargs['shortcode']

        shortened_url = get_object_or_404(ShortenedUrl, shortcode=shortcode)
        context['shortened_url'] = shortened_url
        return context


class RedirectUrlView(RedirectView):
    
    def get_redirect_url(self, *args, **kwargs):
        shortcode = kwargs['shortcode']
        return get_object_or_404(ShortenedUrl, shortcode=shortcode).url