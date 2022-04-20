#from django.contrib import admin
from django.urls import path
from . import views

app_name = 'film'
urlpatterns = [
    #path('film/', include('film.urls')),
    #path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('<int:film_id>/', views.detail, name='detail'),
    path('<int:film_id>/results/', views.results, name='results'),
    path('<int:film_id>/vote/', views.vote, name='vote'),
    path('movies/', views.movies, name='movies'),
]