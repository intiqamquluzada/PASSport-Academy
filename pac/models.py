from django.db import models
from services.mixin import SlugMixin, DateMixin
from services.uploader import Uploader
from services.generator import Generator
from services.choices import EDUCATION_DEGREE, MEET_TYPE


class Students(DateMixin, SlugMixin):
    pp = models.ImageField(upload_to=Uploader.upload_photo_for_students)
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
        ordering = ("-created_at",)
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=Students)
        super(Students, self).save(*args, **kwargs)


class Blog(DateMixin, SlugMixin):
    photo = models.ImageField(upload_to=Uploader.upload_photo_for_blog)
    head = models.CharField(max_length=255)
    main_part = models.TextField()

    def __str__(self):
        return self.head[:8]

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Bloq"
        verbose_name_plural = "Bloqlar"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=Blog)
        super(Blog, self).save(*args, **kwargs)


class Consultation(DateMixin, SlugMixin):
    name = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    meet_date = models.DateTimeField(null=True, blank=True)

    gpa = models.FloatField()
    language_certificate = models.TextField(null=True, blank=True)
    interest_country = models.CharField(max_length=255, null=True, blank=True)
    interested_scholarship_programs = models.CharField(max_length=255, null=True, blank=True)
    work_experience = models.CharField(max_length=255, null=True, blank=True)
    is_met = models.BooleanField(default=False, null=True, blank=True)
    meet_type = models.CharField(choices=MEET_TYPE, default="Offline", max_length=20, null=True, blank=True)
    education_degree = models.CharField(choices=EDUCATION_DEGREE, default="Bakalavr", max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name + " " + self.surname + " --> " + self.interest_country

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Konsultant"
        verbose_name_plural = "Konsultantlar"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=Consultation)
        super(Consultation, self).save(*args, **kwargs)
