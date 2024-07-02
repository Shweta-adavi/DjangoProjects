from django.shortcuts import render
from myapp.forms import StudentForm
# Create your views here.
def formView(request):
    f=StudentForm()
    if request.method=="POST":
        f=StudentForm(request.POST)
        if f.is_valid():
            sid=f.cleaned_data['sid']
            sname=f.cleaned_data['sname']
            smarks=f.cleaned_data['smarks']
            splace=f.cleaned_data['splace']
            d={'id':sid,'name':sname,'marks':smarks,'place':splace}
            return render(request,'myapp/output.html',d)
    d={'form':f}
    return render(request,'myapp/input.html',d)
