from django.db import models

# Create your models here.

class CourseManager(models.Manager):
  def create_course(self, form):
    course_id = Course.objects.create(
      name = form['name']
    )

    description =  Description.objects.create(content=form['description'], course=course_id)
    description.save()

class Course(models.Model):
  name = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = CourseManager()
  def __repr__(self):
    return "<Course : {}>".format(self.name)
  def __str__(self):
        return "<Course: %s>" % self.name

class Description(models.Model):
  content = models.TextField()
  course = models.OneToOneField(Course, primary_key=True, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = CourseManager()
  def __repr__(self):
    return "<Description : {}>".format(self.content)
  def __str__(self):
    return "<Description: %s>" % self.content


