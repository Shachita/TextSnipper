import uuid
import jwt

from django.db import models
from django.urls import reverse
from django.utils import text
from django.utils.text import slugify
from django.utils.timezone import now


class TextSnippet(models.Model):
    shareable_text = models.TextField()
    slug = models.SlugField(unique=True)
    date_time = models.DateTimeField(auto_now_add=True, blank=True)
    secret_key = models.CharField(blank=True, null=True, max_length=100)

    # def __str__(self):
    #     return self.title

    def get_absolute_url(self):
        return reverse("webapp:shareable", kwargs={"slug": self.slug})

    def get_slug(self):
        uuid_value = str(uuid.uuid4())
        unique_slug = slugify(uuid_value[0:13])
        return unique_slug

    def save(self, *args, **kwargs):
        self.shareable_text = jwt.encode({'shareable_text': self.shareable_text}, self.secret_key, algorithm="HS256")
        self.slug = self.get_slug()
        return super(TextSnippet, self).save(*args, **kwargs)
