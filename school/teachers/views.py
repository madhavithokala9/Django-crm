from django.shortcuts import render, redirect
from .models import Teacher

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, "index.html", {"allteachers": teachers})

def add_teacher(request):
    if request.method == "POST":
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        image = request.FILES.get('image')

        Teacher.objects.create(
            name=name,
            subject=subject,
            contact=contact,
            email=email,
            image=image if image else None
        )
        return redirect("all-teachers")

    return render(request, "index.html")

def update_teacher(request, id):
    teacher = Teacher.objects.get(id=id)  

    if request.method == "POST":
        teacher.name = request.POST.get('name')
        teacher.subject = request.POST.get('subject')
        teacher.contact = request.POST.get('contact')
        teacher.email = request.POST.get('email')
        image = request.FILES.get('image')

        if image:
            teacher.image = image

        teacher.save()
        return redirect("all-teachers")

    return render(request, 'index.html', {'teacher': teacher})  

def delete_teacher(request, id):
    Teacher.objects.filter(id=id).delete()
    return redirect("all-teachers")
