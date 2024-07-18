from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django import template
from django.urls import reverse
import misaka

User = get_user_model()
register = template.Library()


class Group(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(blank=True, default='', editable=False)
    members = models.ManyToManyField(User, through='Member')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']


class Member(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='memberships')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_groups')

    def __str__(self):
        return self.user.name

    class Meta:
        unique_together = ('user', 'group')

