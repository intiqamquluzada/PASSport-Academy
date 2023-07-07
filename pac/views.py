from django.shortcuts import render
from .models import Students, Blog


def home_view(request):
    students = Students.objects.all()
    scholarship_students_percent = ((Students.objects.filter(scholarship=True).count())//(Students.objects.all().count()))*100

    last_blog = Blog.objects.last()
    blogs = Blog.objects.all().reverse()[1:]
    context = {
        "students": students,
        "scholarship_students_percent": scholarship_students_percent,
        "last_blog": last_blog,
        "blogs": blogs,


    }

    return render(request, "homepage_1.html", context)
