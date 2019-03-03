from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Course
from .models import Description
# Create your views here.

def index(request):
  context = {
    "courses": Course.objects.order_by("-created_at"),
  }
  return render(request, 'main/index.html', context)


def create(request):
  print(request.POST)
  Course.objects.create_course(request.POST)
  return redirect("/")


def destroy(request, course_id):
  print(course_id)
  context = {
    "course": Course.objects.get(id=course_id)
  }
  return render(request, 'main/delete.html', context)
  # return redirect("/")


def delete(request, course_id):
  cour= Course.objects.get(id=course_id)
  cour.delete()
  return redirect("courses:index")