from django.shortcuts import render, redirect
from .forms import RegCustomer, RegBike, Return_form, RegRoute, RegBranch
from .models import CustomerModel, BikeModel, BranchModel, Return_bike

# Create your views here.
def home(request):    
    if request.method == "POST":
        form = RegCustomer(request.POST)
    
        if form.is_valid():
            namez = form.cleaned_data['name']
            telz = form.cleaned_data['tel']
            bikez = form.cleaned_data['bike']
            routez = form.cleaned_data['route']
            branchz = form.cleaned_data['branch']
            timez = form.cleaned_data['time']

            customer =  CustomerModel(name=namez, 
                                    telephone_number=telz, 
                                    bike=bikez, 
                                    route=routez, 
                                    branch=branchz,
                                    departure_time=timez)
            customer.save()
            form = RegCustomer()
            return render(request, "main/home.html", {"form":form})
    else:
        form = RegCustomer()
        return render(request, "main/home.html", {"form":form})


def bike(request):
    if request.method == "POST":
        reg_bike = RegBike(request.POST)

        if reg_bike.is_valid():
            try:
                names = reg_bike.cleaned_data['name']
                type = reg_bike.cleaned_data['type']
                wheelz = reg_bike.cleaned_data['wheels']
                weight_ = reg_bike.cleaned_data['weight']
                mtrl = reg_bike.cleaned_data['material']
                cd = reg_bike.cleaned_data['condition']
        
                bike = BikeModel(name=names, bike_type=type, wheels=wheelz, weight=weight_, material=mtrl, condition=cd)
                bike.save()
                reg_bike = RegBike()
                return render(request, "main/bike.html", {"form":reg_bike})
            except:
                print("Error while registering a bike")
    else:
        reg_bike = RegBike()
        return render(request, "main/bike.html", {"form":reg_bike})


def return_bike(request):
    if request.method == "POST":
        bike_form = Return_form()

        if bike_form.is_valid:
            cusID = bike_form.cleaned_data['customer_id']
            bikeID = bike_form.cleaned_data['bike_id']
            branchID = bike_form.cleaned_data['branch_id']
            time = bike_form.cleaned_data['return_time']

            bike_form = Return_bike(customer_id=cusID, bike_id=bikeID, branch_id=branchID, return_time=time)
            bike_form.save()
            bike_form = Return_form()
            return render(request, "main/html", {"form": bike_form})
        
    else:
        bike_form = Return_form()
    return render(request, "main/return.html", {"form":bike_form})


# reports page
def reports(request):
    try:
        bikes_ = BikeModel.objects.all()
        return render(request, "main/reports.html", {"bikes_":bikes_})
    except:
        print("Error")

def update(request, bike_id):
    bikes_ = BikeModel.objects.get(bike_id=bike_id)
    form = RegBike(request.POST, instance = bikes_)
    if form.is_valid():
        try:
            names = form.cleaned_data['name']
            type = form.cleaned_data['type']
            wheelz = form.cleaned_data['wheels']
            weight_ = form.cleaned_data['weight']
            mtrl = form.cleaned_data['material']
            cd = form.cleaned_data['condition']
        
            bike = BikeModel(name=names, bike_type=type, wheels=wheelz, weight=weight_, material=mtrl, condition=cd)
            bike.save()
            return render(request, "main/bike.html", {"bike":bikes_})
        except:
            pass

    return render(request, "main/reports.html", {"bikes_":bikes_})

def dlt(request, bike_id):
    bikes_ = BikeModel.objects.get(bike_id=bike_id)
    bikes_.delete()
    return redirect("/reports")

def branch(request):
    if request.method == 'POST':
        branch_ = RegBranch(request.POST)

        if branch_.is_valid():
            n = branch_.cleaned_data['name']
            mgr = branch_.cleaned_data['manager']

            new_branch = BranchModel(name=n, manager=mgr)
            new_branch.save()
            branch_ = RegBranch()
            return render(request, "main/branch.html", {"form": branch_})
    
    else:
        branch_ = RegBranch()
        return render(request, "main/branch.html", {"form": branch_})


def adminn(request):
    return render(request, "main/adminn.html", {})