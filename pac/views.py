from django.contrib import messages
from django.shortcuts import render
from .models import Students, Blog
from .forms import ConsultantForm, MiddleContact
from django.shortcuts import redirect


def home_view(request):
    students = Students.objects.all()
    scholarship_students_percent = ((Students.objects.filter(scholarship=True).count()) // (
        Students.objects.all().count())) * 100

    last_blog = Blog.objects.last()
    blogs = Blog.objects.all().reverse()[1:]

    form = ConsultantForm()
    if request.method == "POST":
        form = ConsultantForm(request.POST or None)
        print('method post olur')
        print(form.errors)
        if form.is_valid():
            print('formda hersey duzdur')
            form.save()
            return redirect("pac:home")
        else:
            form = ConsultantForm()

    form_2 = MiddleContact()
    if request.method == "POST":
        form_2 = MiddleContact(request.POST or None)
        print('method post olur')
        print(form_2.errors)
        if form_2.is_valid():
            print('formda hersey duzdur')
            form_2.save()
            return redirect("pac:home")
        else:
            form_2 = MiddleContact()

    context = {
        "students": students,
        "scholarship_students_percent": scholarship_students_percent,
        "last_blog": last_blog,
        "blogs": blogs,
        "form": form,
        "form_2": form_2,

    }

    return render(request, "homepage_1.html", context)
