from django.urls import path
from . import views

urlpatterns = [
    path("owner/",views.ownerDashboardView,name="owner_dashboard"),
    path("user/",views.userDashboardView,name="user_dashboard"),
    path("createparking/",views.createParking,name="create_parking"),
    path("create-order/",views.create_razorpay_order,name="create_order"),
    path("booking/",views.booking,name="booking"),
    path("verify-payment/",views.verify_razroypay_payment,name="verify_payment"),
    
]