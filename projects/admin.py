from django.contrib import admin


from .models import Student
from .models import Registration 
from .models import Content 
from .models import Course 
 

admin.site.register(Student)
admin.site.register(Registration)
admin.site.register(Content)
admin.site.register(Course)
