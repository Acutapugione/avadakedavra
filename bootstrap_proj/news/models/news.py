from django.db import models
from . author import Author


class News(models.Model):
    pub_date = models.DateTimeField("date published")
    head = models.CharField(max_length=255)
    article = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self) -> str:
        if self.author:
            return f"Author: {self.author}\nHead: {self.head}\nArticle: {self.article[:150]}"
        return f"Head: {self.head}\nArticle: {self.article[:150]}"
        # return super().__str__()
