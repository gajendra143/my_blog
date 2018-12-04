from django.db import models


class BlogTable(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        # __str__ = string representation of an object
        return self.title
