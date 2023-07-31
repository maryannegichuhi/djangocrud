from django.shortcuts import render, redirect
from crudapp.models import Students
from crudapp.forms import StudentForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = StudentForm()
        return render(request, 'index.html', {'form': form})


def show(request):
    students = Students.objects.all()
    return render(request, 'show.html', {'students': students})


def edit(request , id):
    students = Students.objects.get(id=id)
    return render(request, 'edit.html', {'students': students})


def delete(request, id):
    students = Students.objects.get(id=id)
    students.delete()
    return redirect('/show')


def update(request, id):
    students = Students.objects.get(id=id)
    form = StudentForm(request.POST, instance=students)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        return render(request, 'edit.html', {'students': students})
