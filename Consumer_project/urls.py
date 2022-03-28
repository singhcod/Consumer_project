"""Consumer_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employee_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/',views.EmployeeListView,name='employees'),
    path('employees/<int:pk>',views.EmployeeDetailView,name='employees_detail'),
    path('employees/create/',views.EmployeeCreateView,name='employees_create'),
    path('employees/<int:pk>/update/',views.EmployeeUpdataView,name='employees_update'),
    path('employees/<int:pk>/delete/',views.EmployeeDeleteView,name='employees_delete'),

    #for accessing api on single page
    path('providerapi/',views.get_access_providerapi,name='providerapi'),

]
