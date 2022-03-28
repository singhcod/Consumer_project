from django import forms


class EmployeeFrom(forms.Form):
    eno = forms.IntegerField()
    ename = forms.CharField()
    salary = forms.DecimalField()
    address = forms.CharField()
    mobile = forms.IntegerField()
