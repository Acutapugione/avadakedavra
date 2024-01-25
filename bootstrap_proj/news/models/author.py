from django.db import models


class Author(models.Model):
    nickname = models.CharField(max_length=50)

