from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .decorators import role_required
from .forms import ParkingSlotCreationForm
import razorpay
from django.conf import settings
from django.http import JsonResponse


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



def booking(request):
    return render(request,"parking/user/booking.html")

def create_razorpay_order(request):
    #razorpay auth
    client = razorpay.Client(auth=("rzp_test_SQaRVCgAbF3rtY","Kmo8VIjqPBfb57GMdQwr41i0"))
    payment = client.order.create({
        "amount":10000, #paisa
        "currency":"INR",
        "payment_capture":"1"
    })
    return JsonResponse(payment)


def verify_razroypay_payment(request):
    if request.method == "POST":
        client = razorpay.Client(auth=("add yours","add yours"))
        params = {
            "razorpay_order_id": request.POST.get("razorpay_order_id"),
            "razorpay_payment_id": request.POST.get("razorpay_payment_id"),
            "razorpay_signature": request.POST.get("razorpay_signature"),
        }
        print(f"Verifying payment with params: {params}")
        try:
            client.utility.verify_payment_signature(params)
            # Here you would typically save the booking/payment info to your database
            return JsonResponse({"status":"success"})
        except Exception as e:
            print(f"Verification failed: {e}")
            return JsonResponse({"status":"error", "message": str(e)})
    return JsonResponse({"status":"error", "message": "Invalid request method"})