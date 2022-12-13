from django.db import models
import uuid

class Student(models.Model):
    
    id = models.UUIDField(default= uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    age = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    

class Registration(models.Model):
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, null=True, blank=True)
    id = models.UUIDField(default= uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.id


class Content(models.Model):
    
    id = models.UUIDField(default= uuid.uuid4, unique=True, primary_key=True, editable=False)
    des = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.id


class Course(models.Model):
    
    # registration = models.foreign_key(Registration, on_delete=models.SET_NULL)
    id = models.UUIDField(default= uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    contents = Content.objects.all()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


