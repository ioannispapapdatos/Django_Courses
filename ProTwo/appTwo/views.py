from django.shortcuts import render
# from django.http import HttpResponse

from appTwo.forms import newUserForm

# from appTwo.models import User

# Create your views here.


def index(request):
    return render(request,'appTwo/index.html')

def users(request):


    form=newUserForm()

    if request.method =='POST':
        form=newUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print('ERROR FORM Invalid')

    return render(request,'appTwo/users.html',{'form':form})
        

    
