from django.urls import path
from .views import *

urlpatterns=[
    path('index/',index),
    path('agencylogin/',AgencyLogin),
    path('agencyregister/',AgencyRegister),
    path('agencyprofile/',agencyprofile),
    path('aboutus/',aboutus),
    path('contactus/',contactus),
    path('uploadpackages/',uploadview),
    path('packagedisplay/', displayview),
    path('deletepackage/<int:id>',deletepackage),
    path('editpackage/<int:id>',editpackage),

    path('userregister/',UserRegisterView),
    path('userlog/',UserLoginView),
    path('userprofile/',userprofile),
    path('allpackages/',packageview),
    path('bookpackage/<int:id>',userbook),

    path('emailalert/',emailalert),
    path('addtowishlist/<int:id>',wishlist),
    path('wishdetail/',wishdetail),
    path('removewish/<int:id>',removewish),
    path('bookeduser/',bookedusersdisplay),
    path('confirmationmail/<int:id>',agencyconfirm),

    path('agencydetails/',agencydetails),
    path('userbiodetails/<int:id>',userbio),
    path('displaybio/',displaybio),
    path('placedetails/',searchbox)
]