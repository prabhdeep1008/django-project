from django.shortcuts import render,redirect
from myapp.form import EmployeeForm 

# Create your views here.
def index(request):  
    form = EmployeeForm
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            form.save()
            try:  
                return redirect('/a')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})