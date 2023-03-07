
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect


from . models import User_details,District,Branches


# Create your views here.

# login
def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pswd = request.POST['password']
        user = auth.authenticate(username=uname,password=pswd)
        if user is not None:
            auth.login(request,user)
            print("user logged")
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            print("login error")
            return redirect('login')
    return render(request,'login.html')

# register
def register(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pswd = request.POST['pswd']
        cpswd = request.POST['cpswd']
        if pswd == cpswd:
            if User.objects.filter(username=uname).exists():
                messages.info(request, "Username already taken")
                return redirect('registers')
            else:
                user = User.objects.create_user(username=uname, password=pswd)
                user.save()
                return redirect('login')
                print('User Created')
        else:
            messages.info(request, "Password not match")
            return redirect('register')
            print("User not created")
        return redirect('/')
    return render(request, 'register.html')

# logout
def logout(request):
    auth.logout(request)
    return redirect('/')

# register user details
def user_details(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phno = request.POST['phno']
        mail = request.POST['mail']
        address = request.POST['address']
        districts = request.POST['district']
        district = District.objects.get(pk=districts)
        branch = request.POST['branch']
        branches = Branches.objects.get(pk=branch)
        account = request.POST['account']
        material = request.POST.getlist('checks[]')
        register = User_details(name=name, dob=dob, age=age, gender=gender, phno=phno, mailid=mail,
                                addres=address, district=district, branch=branches, account_type=account, materials=material)
        register.save()
        messages.success(request, 'Registration accepted')
        # return redirect('/')
    district = District.objects.all()
    return render(request,'user_details_register.html',{'districts': district})

# for branch dropdownlist based on district
def get_branches_ajax(request):
    if request.method == "POST":
        dist_id = request.POST['dist_id']
        try:
            district = District.objects.filter(id = dist_id).first()
            branches = Branches.objects.filter(district = district)
        except Exception:
            data['error_message'] = 'error'
            return JsonResponse(data)
        return JsonResponse(list(branches.values('id', 'bname')), safe = False)