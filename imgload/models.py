from django.db import models
from urllib.request import urlretrieve
from django.core.files import File
import os

class Image_model(models.Model):
    img = models.ImageField(upload_to='images', blank=True)
    url = models.URLField(max_length=200, blank=True)

    def cache(self):
        if self.url and not self.img:
            result = urlretrieve(self.url)
            print(os.path.basename(self.url))
            self.img.save(
                os.path.basename(self.url),
                File(open(result[0], 'rb'))
            )

    def save(self, *args, **kwargs):
        self.cache()
        super().save()

    # def __str__(self):
    #     if self.url:
    #         return self.url
    #     return self.img
