from django.db import models


class Comment(models.Model):
    title = models.CharField('Name', max_length=50)
    comment = models.TextField('Comment', max_length=1000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'