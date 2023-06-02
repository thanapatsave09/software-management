#คำสั่งทั้งหมดนี้จะแสดงที่หน้าเพิ่มข้อมูลพนักงานใหม่
from django import forms
from taskapp.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"
        labels={             
            'fname':'ชื่อ',
            'lname':'นามสกุล',
            'address':'ที่อยู่',
            'gender':'เพศ',
            'birthdate':'วันเกิด',
            'department':'แผนก',
            'phone':'เบอร์โทรศัพท์',
            'cover':'ภาพพนักงาน'
        }
        widgets={
            'address':forms.Textarea(attrs={'rows':'3'}),
            'gender':forms.RadioSelect(),
            'birthdate':forms.DateInput(attrs={'type':'date'})
        }