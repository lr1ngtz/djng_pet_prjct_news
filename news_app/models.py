from django.db import models
from django.db.models.fields import BooleanField


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Published at'
    )
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(
        default=True,
        verbose_name='Is published?'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'News'
        ordering = ['-created_at']
