from django.db import models
from services.mixin import SlugMixin, DateMixin
from services.uploader import Uploader
from services.generator import Generator


class Students(DateMixin, SlugMixin):
    pp = models.ImageField(upload_to=Uploader.upload_menu_to_restaurants)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    won_country = models.CharField(max_length=200)
    won_city = models.CharField(max_length=200)
    won_university = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    scholarship = models.BooleanField()
    description = models.TextField()

    def __str__(self):
        return self.name + " " + self.surname

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=Students)
        super(Students, self).save(*args, **kwargs)
