from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import ShortenUrlForm

# Create your views here.
class IndexView(FormView):
    template_name = 'shortener/index.html'
    form_class = ShortenUrlForm
    success_url = ''

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)