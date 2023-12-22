# views.py

from .forms import AlbumForm
from .models import Album
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Musician, Album
from .forms import MusicianForm, AlbumForm


class MusicianListView(ListView):
    model = Musician
    template_name = 'musician_list.html'
    context_object_name = 'musicians'


class MusicianCreateView(LoginRequiredMixin, CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musician_form.html'
    success_url = reverse_lazy('musician_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MusicianUpdateView(LoginRequiredMixin, UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musician_form.html'
    success_url = reverse_lazy('musician_list')


class MusicianDeleteView(LoginRequiredMixin, DeleteView):
    model = Musician
    template_name = 'musician_form.html'
    success_url = reverse_lazy('musician_list')
    # pass type
    type = 'delete'


class AlbumListView(ListView):
    model = Album
    template_name = 'album_list.html'
    context_object_name = 'albums'


class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album_form.html'
    success_url = '/albums/'

    def form_valid(self, form):
        # Additional logic if needed
        return super().form_valid(form)


class AlbumUpdateView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album_form.html'
    success_url = reverse_lazy('album_list')


class AlbumDeleteView(LoginRequiredMixin, DeleteView):
    model = Album

    template_name = 'album_form.html'
    success_url = reverse_lazy('album_list')
