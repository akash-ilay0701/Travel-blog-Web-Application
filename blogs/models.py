from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

class TravelBlog(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    description = RichTextField(null=True, blank=True)
    thumbnail = models.CharField(max_length=500)

    def __str__(self):
        return self.title + " | " + str(self.author)
    # def get_absolute_url(self):
    #     return reverse("confirmed")








