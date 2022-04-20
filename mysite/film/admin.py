from django.contrib import admin

from .models import Movie
from .models import Episode
from .models import Category
from .models import Choice

admin.site.register(Movie)
admin.site.register(Episode)
admin.site.register(Category)
admin.site.register(Choice)
# Register your models here.
