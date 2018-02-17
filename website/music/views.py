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


class IndexView(generic.ListView):
    template_name = 'music/index.html'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'
