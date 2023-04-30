from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


class Course(models.Model):
    course = models.CharField(primary_key=True, max_length=50)
    # student = models.ManyToManyField(StudentDetail, verbose_name=("students detail"))
    # student = models.OneToOneField(StudentDetail, on_delete=models.CASCADE)
    def __str__(self):
        return self.course
    
    class Meta:
        db_table ='Course'
    
class StudentDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(("first name"), max_length=50)
    # subject = models.CharField(("Subject"), max_length=50)
    enrollmentno = models.IntegerField(("roll no"))
    phone = models.BigIntegerField()
    email = models.EmailField(("Email"), max_length=254)
    course = models.ForeignKey(Course,on_delete=models.CASCADE, null=True)
    is_present = models.BooleanField(("Present"), default=False)
    image = models.ImageField(upload_to='profilepic')
    # ecoding = models.AutoField()
    date = models.DateField("Date", auto_now_add=True)
    updated = models.DateTimeField( auto_now=True)
    def __str__(self):
        return self.name 
    
class ProfessorDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(("Mentor name"), max_length=50)
    phone = models.BigIntegerField(("Phone no"))
    subject = models.CharField('Subject', max_length=50)
    
    def __str__ (self):
        return self.name 
    
    
    class Meta:
        db_table = 'Mentor_Detail'

   
    