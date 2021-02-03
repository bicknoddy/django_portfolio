from test_site.settings import STATIC_ROOT, STATIC_URL
from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField()
    long_description = models.TextField()
    slug = models.SlugField(max_length=40)

    categories = [('Programming', 'Programming'),
                  ('Photography', 'Photography'),
                  ('Data', 'Data'),
                  ('Misc', 'Misc')
    ]

    category = models.CharField(max_length=15, choices=categories)

    #if zip file for a programming project
    file = models.FileField(upload_to='files/', blank=True)

    def __str__(self):
        return self.title