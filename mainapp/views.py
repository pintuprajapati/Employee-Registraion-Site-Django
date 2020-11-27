from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from users.forms import UserRegisterForm
from .models import Employee

# Create your views here.
def home(request):
    return render(request, 'mainapp/index.html')

@login_required
def add_emp(request):
    return render(request, 'mainapp/addEmp.html')

@login_required
def all_emp(request):
    all_employees = Employee.objects.all()
    return render(request, 'mainapp/allEmp.html', {'all_employees': all_employees})

def update_emp(request, id):
    empl = Employee.objects.get(id=id)
    form = UserRegisterForm(request.POST)
    # form = UserRegisterForm(request.POST or None, instance=empl)

    if form.is_valid():
        form.save()
        return redirect('allEmp.html')
    return render(request, 'mainapp/update_emp.html', {'form': form, 'empl': empl})

def delete_emp(request, id):
    empl = Employee.objects.get(id=id)

    if request.method == "POST":
        empl.delete()
        return redirect('all_emp')
    return render(request, 'mainapp/delete_emp.html', {'empl': empl})

def add_emp_submission(request):
    firstname = request.POST["firstname"]
    lastname = request.POST["lastname"]
    empId = request.POST["empId"]
    empEmail = request.POST["empEmail"]
    address = request.POST["address"]
    city = request.POST["city"]
    phone = request.POST["phone"]
    birthday = request.POST["birthday"]

    ## created "employee" Variable for "Employee" class/model. (Saving Data from FORM to MODEL/DATABASE)
    ## After that assigned forms variable to models field.
    employee = Employee(firstname=firstname, lastname=lastname,emp_id=empId, email_id=empEmail, address=address, city=city, mobile=phone, birthday=birthday)
    employee.save()

    return render(request, 'mainapp/addemp.html')
