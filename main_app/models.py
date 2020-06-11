import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from PIL import Image
from PIL.ExifTags import TAGS

# Create your models here.


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    uploaded_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)

    class Meta:
        permissions = [
            ('special_status', 'Can see all pictures'),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('image_detail', kwargs={'pk': str(self.pk)})

    @property
    def exif(self):
        exif = {}
        image_data = Image.open(self.image)
        for tag, value in image_data._getexif().items():
            if tag in TAGS:
                exif[TAGS[tag]] = value
        return exif
