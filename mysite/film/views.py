from django.http import HttpResponse, HttpResponseRedirect
from .models import Movie, Episode, Category, Choice
#from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
#from django.template import loader

def index(request):
    #return HttpResponse("Hello, world. You're at the film index.")
    latest_list = Movie.objects.order_by('-pub_date')[:5]
    context = {'latest_list': latest_list}
    return render(request, 'film/index.html', context)
    

def detail(request, film_id):
    movie = get_object_or_404(Movie, pk=film_id)
    #episode = get_object_or_404(Episode, pk=film_id)
    #category = get_object_or_404(Category, film_id)
    return render(request, 'film/detail.html', {'movie': movie})


def movies(request):
    movie_list = Movie.objects.order_by('-pub_date')[:5]
    series_list = Episode.objects.order_by('-pub_date')[:5]
    return render(request, 'film/movies.html', {
            'movie_list': movie_list,
            'series_list': series_list,
    })
def results(request, film_id):
    movie = get_object_or_404(Movie, pk=film_id)
    return render(request, 'film/results.html', {'movie': movie})

def vote(request, film_id):
    movie = get_object_or_404(Movie, pk=film_id)
    try:
        selected_choice = movie.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'film/detail.html', {
            'movie': movie,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('film:results', args=(movie.id,)))
