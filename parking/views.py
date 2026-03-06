from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .decorators import role_required
from .forms import ParkingSlotCreationForm

# Create your views here.
#@login_required(login_url="login") #check in core.urls.py login name should exist..
@role_required(allowed_roles=["owner"]) #check in core.urls.py login name should exist..
def ownerDashboardView(request):
    return render(request,"parking/owner/owner_dashboard.html")

#@login_required(login_url="login")
@role_required(allowed_roles=["user"]) #check in core.urls.py login name should exist.. 
def userDashboardView(request):
    return render(request,"parking/user/user_dashboard.html")


def createParking(request):
    if request.method =="POST":
        print(request.POST)
        form = ParkingSlotCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("owner_dashboard")
            #return render(request,"htm",{parkings:parking})
    else:
        form = ParkingSlotCreationForm()
    return render(request,"parking/owner/create_parking.html",{"form":form})