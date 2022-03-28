from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
# view for communocating with provides project
import requests
import json
from django.http import HttpResponse

#getting all data from the provider app
def EmployeeListView(request):
    response = requests.get('http://127.0.0.1:8000/api/emplopyees/') #sending request to the prover app

    if response.status_code == 200:
        context = {
            "employee_list":json.loads(response.text)

        }
        return render(request,'employee_app/employee_list.html',context)
    else:
        context = {
            "error" : "Employees data is not available in database"
        }
        return render(request, 'employee_app/employee_list.html',context)


#geting single one record form the provider app

def EmployeeDetailView(request,pk):
    response = requests.get('http://127.0.0.1:8000/api/emplopyees/'+str(pk)+'/')  # sending request to the prover app

    if response.status_code == 200:
        context = {
            "employee": json.loads(response.text)

        }
        return render(request, 'employee_app/employee_detail.html', context)
    else:
        context = {
            "error": "Employees data is not available in database"
        }
        return render(request, 'employee_app/employee_detail.html', context)


#post data to 
from employee_app.forms import EmployeeFrom
def EmployeeCreateView(request):
    if request.method == 'POST':
        form = EmployeeFrom(request.POST)
        if form.is_valid():
            eno = request.POST.get("eno")
            ename = request.POST.get("ename")
            salary = request.POST.get("salary")
            address= request.POST.get("address")
            mobile= request.POST.get("mobile")

            emp_object = {
                "eno":eno,
                "ename":ename,
                "salary":salary,
                "address":address,
                "mobile":mobile
            }
            response = requests.post('http://127.0.0.1:8000/api/emplopyees/',data=emp_object)
            if response.status_code == 201:
                context = {
                  "data":json.loads(response.text)
                }
            else:
                context = {
                    "error":"Requested Data is Not Created Successfully"
                }
            return render(request,'employee_app/employee_form.html',context)

        else:
            context = {
                "error" : "Please Send Proper Data For Creating"
            }
            return render(request, 'employee_app/employee_form.html', context)

    else:
        form = EmployeeFrom()
        return render(request,'employee_app/employee_form.html',{'form':form})



def EmployeeUpdataView(request,pk):
    if request.method == "POST":
        form = EmployeeFrom(request.POST)
        if form.is_valid():
            eno = request.POST.get("eno")
            ename = request.POST.get("ename")
            salary = request.POST.get("salary")
            address = request.POST.get("address")
            mobile = request.POST.get("mobile")

            emp_object = {
                "eno": eno,
                "ename": ename,
                "salary": salary,
                "address": address,
                "mobile": mobile
            }
            response = requests.put('http://127.0.0.1:8000/api/emplopyees/'+str(pk)+'/', data=emp_object)
            if response.status_code == 200:
                return redirect('/employees/')

            elif response.status_code == 400:

                contaxt = {
                    'message':"Employee Object Is Not Update Successfully"
                }
            else:

                contaxt = {
                    'message':"Sorry You Are Unable To Update Data Usingh This Api"
                }
            return render(request, 'employee_app/employee_update.html', contaxt)

        else:
            contaxt = {
                'message': 'Please Send All Fields Data Properly'
            }
        return render(request,'employee_app/employee_update.html',contaxt)
    else:
        response = requests.get('http://127.0.0.1:8000/api/emplopyees/'+str(pk)+'/')

        if response.status_code == 200:
            try:
                employee = json.loads(response.text)     #convert json data into dictonary
                context = {
                    'employee':employee
                }
            except:
                context = {
                    'error':'Sorry You Unable To Access The Data Using This Api'
                }
        else:
            context = {
                'error' :'Requested record is not available in database'
            }
        return render(request,'employee_app/employee_update.html',context)


def EmployeeDeleteView(request,pk):
    if request.method == 'POST':
        response = requests.delete('http://127.0.0.1:8000/api/emplopyees/' + str(pk) + '/')
        if response.status_code == 204:
            return redirect("/employees/")
            # messgae = "Record deleted successfully"
            # contaxt = {
            #     'message':messgae
            # }
        elif response.status_code ==  404:
            contaxt = {
                'error':'Requested record is not available to deleting'
            }
        else:
            contaxt = {
                'error':'You Are unbale to delete the record using this api'
            }
        return render(request,'employee_app/employee_delete.html',contaxt)
    else:
        response = requests.get('http://127.0.0.1:8000/api/emplopyees/' + str(pk) + '/')

        if response.status_code == 200:
            try:
                employee = json.loads(response.text)  # convert json data into dictonary
                contaxt = {
                    'employee': employee
                }
            except:
                contaxt = {
                    'error': 'Sorry You Unable To Access The Data Using This Api'
                }
        else:
            contaxt = {
                'error': 'Requested record is not available in database'
            }
        return render(request, 'employee_app/employee_delete.html', contaxt)



#views for accessiapi on singlen page through the provider api
def get_access_providerapi(request):
    return render(request,'proiver_app/providerapi.html')