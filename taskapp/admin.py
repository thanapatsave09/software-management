from django.contrib import admin
from taskapp.models import Task
from taskapp.models import Employee
from taskapp.models import Statement

class TaskAdmin(admin.ModelAdmin):
    list_display=["name","status","manager"]

class StatementAdmin(admin.ModelAdmin): #ไว้ปรับแต่งหลังบ้านของ admin
    list_display=["name","amount","category"]
    list_per_page = 5 #แสดงผลรายการในหน้า admin ตามจำนวนที่ระบุไว้
    list_editable=["amount","category"] #สามารถแก้ไขได้ในหน้าแรกของ admin
    list_filter=["category","amount"] # เป็นตัวกรองข้อมูลว่าเป็นรายรับหรือรายจ่าย
    search_fields=["name"] #เป็นช่องค้นหาข้อมูลในส่วนของ admin 

# Register your models here.
admin.site.register(Task,TaskAdmin)
admin.site.register(Employee)
admin.site.register(Statement,StatementAdmin)