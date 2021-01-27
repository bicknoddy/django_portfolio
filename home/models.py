from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField()

    long_description = models.TextField(blank=True)

    categories = [('Programming', 'Programming'),
                  ('Photography', 'Photography'),
                  ('Data', 'Data'),
                  ('Misc', 'Misc')
    ]

    category = models.CharField(max_length=15, choices=categories)

    #if zip file for a programming project
    file_upload = models.FileField(blank=True)

    #add photo(s) for data analysis or photography
    photo_upload = models.ImageField(blank=True)

    def __str__(self):
        return self.title