from django.db import models

class CourseType(models.TextChoices):
        SEM = 'SEM', 'Semester',
        YER = 'YER','Yearly',

# Create your models here.
class Course(models.Model):
    name = models.CharField("name", max_length=50,unique=True)
    type = models.CharField(
        max_length=3,
        choices=CourseType.choices,
        default=CourseType.SEM,
    )
    def __str__(self):
            return self.name
    

class Semester(models.Model):
    name = models.CharField("name", max_length=1)
    course = models.ForeignKey("Course",on_delete=models.CASCADE)

    def __str__(self):
        if(self.course.type ==CourseType.SEM):  
            return self.course.name+"'s "+self.name+  " semester"
        return self.course.name+"'s "+self.name+  " year"
    


class Subject(models.Model):
    name =  models.CharField(max_length=50)
    semester = models.ForeignKey("Semester",on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    