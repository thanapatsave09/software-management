from django.shortcuts import render,redirect
from django.http import HttpResponse
from taskapp.models import Task
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from taskapp.forms import EmployeeForm
from taskapp.models import Employee
from django.shortcuts import redirect
from taskapp.models import Statement
from django.db.models import Sum

# Create your views here.
@login_required(login_url="/login")
def index(request):
    if request.method == "POST":
        #ดึงข้อมูลจากฟอร์ม
        name = request.POST["name"]
        #เช็คค่าว่าง
        if name == "":
            #ส่งข้อความแจ้งเตือนผู้ใช้
            messages.warning(request,"กรุณาป้อนชื่อรายการ")
            return redirect("/")
        else :
            #บันทึกข้อมูล
            task=Task.objects.create(name=name,manager=request.user)
            task.save()
            messages.success(request,"บันทึกข้อมูลเรียบร้อย")
            return redirect("/")
    else :
        all_task = Task.objects.filter(manager=request.user)
        #ระบบหมายเลขหน้า
        page = request.GET.get("page")
        paginator = Paginator(all_task,4)
        all_task = paginator.get_page(page)

        return render(request,"index.html",{"all_task":all_task})

@login_required(login_url="/login")
def complete_task(request,task_id):
    task = Task.objects.get(pk=task_id)
    if task.manager == request.user:
        task.status=True
        task.save()
        return redirect('/')
    else:
        messages.warning(request,"คุณไม่มีสิทธิ์เปลี่ยนสถานะ")
        return redirect("/")

@login_required(login_url="/login")
def pending_task(request,task_id):
    task = Task.objects.get(pk=task_id)
    if task.manager == request.user:
        task.status=False
        task.save()
        return redirect('/')
    else :
        messages.warning(request,"คุณไม่มีสิทธิ์เปลี่ยนสถานะ")
        return redirect("/")

def indexemp(request): 
    if request.method == "POST": # ไว้ค้นหาข้อมูล
        name = request.POST["name"]
        all_employee = Employee.objects.filter(fname__contains=name)
        return render(request,"indexemp.html",{"all_employee":all_employee})
    else:
        all_employee = Employee.objects.all()
        return render(request,"indexemp.html",{"all_employee":all_employee})

def create(request):
    print(request)
    if request.method=="POST":
        #บันทึกข้อมูล
        form = EmployeeForm(request.POST,request.FILES) #เอาคำสั่งจาก forms.py มาแสดงหน้า เพิ่มข้อมูลพนักงานใหม่
        if form.is_valid(): #ถ้าส่งข้อมูลมาครบทุกค่า
            form.save() #บันทึก
            return redirect('/indexemp') #รีเทินไปที่หน้าแรก
    else :
        form = EmployeeForm()
        return render(request,"create.html",{"form":form})

def delete(request,emp_id): #ไว้ลบข้อมูลพนักงาน
    emp=Employee.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/indexemp")

def edit(request,emp_id):
    #อัพเดต
    if request.method == "POST":
        emp = Employee.objects.get(pk=emp_id) # ดึงข้อมูลพนักงานที่ต้องการมาแก้ไข
        form = EmployeeForm(instance=emp,data=request.POST) # นำข้อมูลที่แก้ไขมาแทนที่ข้อมูลเดิม
        if form.is_valid(): # บันทึกข้อมูลซ้ำไปที่เดิม
            form.save()
            return redirect("/indexemp") #เปลี่ยนเส้นทางไปที่หน้าแรก
    #โยนข้อมูลไปทำงานในแบฟอร์มแก้ไขข้อมูล
    else:
        emp = Employee.objects.get(pk=emp_id)
        form = EmployeeForm(initial=emp.__dict__)
        return render(request,"edit.html",{"form":form}) # แก้ไขแล้วนำไปแสดงผลบน templates


def indexmoney(request): #ไว้เอา index ไปแสดงผลหน้าเว็บไซ
      total_income = Statement.objects.filter(category="income").aggregate(Sum("amount")) #รายรับทั้งหมด
      total_expense = Statement.objects.filter(category="expense").aggregate(Sum("amount")) #รายจ่ายทั้งหมด
      return render(request,"indexmoney.html",{"income":total_income,"expense":total_expense})

def account(request): #ไว้เอา account ไปแสดงผลหน้าเว็บไซ
      data=Statement.objects.all()
      return render(request,"account.html",{"data":data})
