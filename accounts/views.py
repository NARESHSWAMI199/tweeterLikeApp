from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout 



# Function based  views to class based view

def login_view(request,*args,**kwargs):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        user_ = form.get_user()
        login(request,user_)
        return redirect('/')
    context = {
        'form' : form,
        'btn_label':'login',
        'title': "Login"
    }
    return render(request,"accounts/auth.html", context )


# the userCreation is a Model form so we can use this same as model form

def register_view(request,*args,**kwargs):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        # in case of model form
        user = form.save(commit=True)
        user.set_password(form.cleaned_data.get('password1'))
        # you can send a email verifiaction to their account
        login(request,user_)
        return redirect('/')
    else:
        print("something went wrong")
    context = {
        'form' : form,
        'btn_label' : 'singup',
        'title': "Singup"
    }
    return render(request,"accounts/auth.html",context)

def logout_view(request,*args,**kwargs):
    if request.method == "POST":
        logout(request)
        return redirect('/')
    context = {
        'form' : None,
        'discription': 'Are you sure you want logout ?',
        'btn_label' : 'logout ? ',
        'title': "Logout"
    }
    return render(request,"accounts/auth.html",context)