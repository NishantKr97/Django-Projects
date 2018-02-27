from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Album, Song
#
#
# def index(request):
#     all_albums = Album.objects.all()
#     template = loader.get_template('music/index.html')
#     context = {
#         'all_albums': all_albums,
#     }
#     return render(request, 'music/index.html', context)
#     # return HttpResponse(template.render(context, request))
#
#
# def details(request, album_id):
#     # return HttpResponse("<h2> This is Music Album no. : " + str(album_id) + "</h2>")
#     # albums = Album.objects.get(pk=album_id)
#     albums = get_object_or_404(Album, pk=album_id)
#     return render(request, 'music/detail.html', {'albums': albums})
#
#
# def favourite(request, album_id):
#     albums = get_object_or_404(Album, pk=album_id)
#     try:
#         selected_song = albums.song_set.get(pk=request.POST['song'])
#     except (KeyError, Song.DoesNotExist):
#         return render(request, 'music/detail.html', {
#             'albums': albums,
#             'error_message': "You did not select a valid song"
#         })
#     else:
#         selected_song.is_favourite = True
#         selected_song.save()
#         return render(request, 'music/detail.html', {'albums': albums})


from django.views import generic
from .models import Album, Song
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import Userforms


class IndexView(generic.ListView):
    template_name = 'music/index.html'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumDelte(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


class UserFormView(View):
    form_class = Userforms
    template_name = 'music/registeration_form.html'

    # display form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # post data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            # cleaned(normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.set_username(username)
            user.save()

            # returns User objects if credential are correct
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})

