from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    manager = models.ForeignKey(User,on_delete=models.CASCADE,default=None)

class Employee(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    address = models.TextField()
    gender = models.CharField(
        max_length=15,
        choices=[('ชาย','ชาย'),('หญิง','หญิง'),('เพศทางเลือก','เพศทางเลือก')],
        default='ชาย'
    )
    birthdate=models.DateField()
    department=models.CharField(
        max_length=50,
        choices=[('กราฟิก','กราฟิก'),('IT','IT'),('บัญชี','บัญชี')],
        default='กราฟิก'
    )
    phone = models.IntegerField()
    cover = models.ImageField(upload_to="images",blank=False)

class Statement(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    choices=(
        ("income","รายรับ"),
        ("expense","รายจ่าย")
    )
    category = models.CharField(max_length=100,choices=choices,default=1)
    # อัพตัว models.py ขี้นไปทำงานที่ฐานข้อมูล โดยใช้ python manage.py makemigrations
    def __str__(self):
        return self.name + "|"+str(self.amount) +"|"+self.category