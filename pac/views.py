from django.shortcuts import render
from .models import Students


def home_view(request):
    students = Students.objects.all()
    scholarship_students_percent = ((Students.objects.filter(scholarship=True).count())//(Students.objects.all().count()))*100

    context = {
        "students": students,
        "scholarship_students_percent": scholarship_students_percent,
    }

    return render(request, "homepage_1.html", context)
