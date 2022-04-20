import datetime
from django.db import models
from django.utils import timezone

def upload_location(instance, filename, **kwargs):
    file_path = 'film/movies/{title}-{filename}'.format(
         title=instance.title, filename=filename)
    return file_path



class Movie(models.Model):
    
    title = models.CharField(max_length=50)
    category = models.ForeignKey('Category', models.DO_NOTHING, blank=True, null=True)
    year = models.CharField(max_length = 5)
    text = models.CharField(max_length = 500)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    pub_date = models.DateTimeField('date published')
    url_adress = models.CharField(max_length=400)
    is_series = models.BooleanField()
   
    
    def __str__(self):
        return self.title
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        db_table = 'movies'


class Episode(models.Model):
    title = models.CharField(max_length=50)
    parent_series = models.ForeignKey('Movie', models.DO_NOTHING)
    url_adress = models.CharField(max_length=400)
    year = models.CharField(max_length = 5)
    text = models.CharField(max_length = 500)
    pub_date = models.DateTimeField('date published')
    episode_no = models.IntegerField()
    
    
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'episodes'
        unique_together = (('parent_series', 'episode_no'),)


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'
        verbose_name_plural = 'Categories'
        
class Choice(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
