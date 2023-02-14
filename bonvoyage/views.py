from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
# from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views import generic
from bon_voyage.settings import EMAIL_HOST_USER
from .forms import *
# Create your views here.



def index(request):
    return render(request,'index.html')
def agencylogin(request):
    return render(request,'agencylogin.html')
def agencyregister(request):
    return render(request,'agencyregistration.html')
def agencyprofile(request):
    return render(request,'agencyprofile.html')
def aboutus(request):
    return render(request,'aboutus.html')
def userprofile(request):
    return render(request,'userprofile.html')
def contactus(request):
    return render(request,'contactus.html')


def AgencyLogin(request):
    if request.method=='POST':
        a=agencylogform(request.POST)
        if a.is_valid():
            em=a.cleaned_data['email']
            ps=a.cleaned_data['password']
            b=agencyregmodel.objects.all()
            for i in b:
                agn=i.agency
                request.session['agency']=agn
                if i.email==em and i.password==ps:
                    return render(request,'agencyprofile.html',{'agn':agn})
            else:
                 return HttpResponse("LOGIN FAILED")
    else:
        return render(request,'agencylogin.html')

def AgencyRegister(request):
    if request.method == 'POST':
        a=agencyregform(request.POST)
        if a.is_valid():
            an=a.cleaned_data['agency']
            em=a.cleaned_data['email']
            ad=a.cleaned_data['address']
            ph=a.cleaned_data['phone']
            ps=a.cleaned_data['password']
            cp=a.cleaned_data['cpassword']

            if ps==cp:
                b=agencyregmodel(agency=an,email=em,address=ad,phone=ph,password=ps)
                b.save()
                return redirect(AgencyLogin)
            else:
                return HttpResponse("INCORRECT PASSWORD")

        else:
            return HttpResponse("COMPANY REGISTRATION FAILED...")

    else:
        return render(request,'agencyregistration.html')

# def packageuploadview(request,id):
#     d=agencyregmodel.objects.get(id=id)
#     an=d.agency
#     em=d.email
#     if request.method=='POST':
#         a=uploadform(request.POST)
#         if a.is_valid():
#             an=a.cleaned_data['agency']
#             em=a.cleaned_data['email']
#             ds=a.cleaned_data['destinations']
#             dy=a.cleaned_data['days']
#             ny=a.cleaned_data['nights']
#             st=a.cleaned_data['stay']
#             pt=a.cleaned_data['pet']
#             fd=a.cleaned_data['food']
#             rt=a.cleaned_data['rate']
#
#             b=uploadmodel(agency=an,email=em,destinations=ds,days=dy,nights=ny,stay=st,pet=pt,food=fd,rate=rt)
#             b.save()
#             return redirect(displayview)
#         else:
#             return HttpResponse("failed")
#     else:
#         return render(request,'uploadpackages.html',{'an':an,'em':em})

# def displayview(request):
#     a=uploadmodel.objects.all()
#     # b=request.session['agency']
#     return render(request,'packagedisplay.html',{'a':a})

def uploadview(request):
    d=agencyregmodel.objects.all()
    # ag=d.agency
    # em=d.email
    if request.method=='POST':
        a=uploadform(request.POST)
        if a.is_valid():
            an=a.cleaned_data['agency']
            em=a.cleaned_data['email']
            ds=a.cleaned_data['destina']
            fd=a.cleaned_data['food']
            pt=a.cleaned_data['pet']
            dn=a.cleaned_data['duration']
            st=a.cleaned_data['stay']
            rt = a.cleaned_data['rate']

            b=packageuploadmodel(agency=an,email=em,destina=ds,food=fd,pet=pt,duration=dn,stay=st,rate=rt)
            b.save()
            return redirect(displayview)
        #     return HttpResponse('vacancy uploaded succesfully...')
        else:
            return HttpResponse('failed to upload vacancy...')
    else:
        return render(request,'uploadpackages.html')



def displayview(request):
    a=packageuploadmodel.objects.all()
    b=request.session['agency']
    return render(request,'displaypackage.html',{'a':a,'b':b})

def editpackage(request,id):
    a=packageuploadmodel.objects.get(id=id)
    an=a.agency
    em=a.email
    if request.method=='POST':
        a.agency=request.POST.get('agency')
        a.email=request.POST.get('email')
        a.destina=request.POST.get('destina')
        a.food=request.POST.get('food')
        a.pet=request.POST.get('pet')
        a.duration=request.POST.get('duration')
        a.stay=request.POST.get('stay')
        a.rate = request.POST.get('rate')
        a.save()
        return redirect(displayview)
    return render(request,'editpackage.html',{'a':a,'id':id,'an':an,'em':em})

def deletepackage(request,id):
    a=packageuploadmodel.objects.get(id=id)
    a.delete()
    return redirect(displayview)


def UserRegisterView(request):
    if request.method == 'POST':
        a=userregform(request.POST)
        if a.is_valid():
            nm=a.cleaned_data['name']
            em=a.cleaned_data['email']
            ph = a.cleaned_data['phone']
            ps = a.cleaned_data['password']
            cp = a.cleaned_data['cpassword']

            if ps==cp:
                b=userregmodel(name=nm,email=em,phone=ph,password=ps)
                b.save()
                return redirect(UserLoginView)
            else:
                return HttpResponse("INCORRECT PASSWORD")

        else:
            return HttpResponse("COMPANY REGISTRATION FAILED...")

    else:
        return render(request,'userregistration.html')

def UserLoginView(request):
    if request.method=='POST':
        a=userlogform(request.POST)
        if a.is_valid():
            em=a.cleaned_data['email']
            ps=a.cleaned_data['password']
            b=userregmodel.objects.all()
            for i in b:
                nm=i.name
                request.session['name'] = nm
                if i.email==em and i.password==ps:
                    return render(request,'userprofile.html',{'nm':nm})
            else:
                 return HttpResponse("LOGIN FAILED")
    else:
        return render(request,'userlogin.html')

def packageview(request):
    a=packageuploadmodel.objects.all()
    return render(request,'allpackages.html',{'a': a})

def userbook(request,id):
    b=packageuploadmodel.objects.get(id=id)
    an=b.agency
    ds=b.destina
    rt=b.rate
    if request.method=='POST':
        c=bookform(request.POST)
        if c.is_valid():
            an=c.cleaned_data['agency']
            ds=c.cleaned_data['destina']
            rt = c.cleaned_data['rate']
            nm=c.cleaned_data['name']
            em=c.cleaned_data['email']

            b=bookmodel(agency=an,destina=ds,rate=rt,name=nm,email=em)
            b.save()
        # mail sending function
            subject=f"YOUR TOUR PACKAGE IS BOOKED WITH {an} agency"
            message=f"hi {nm}\n your package booking for {ds} is booked successfully.The agency team will contact you shortly."
            email_from = EMAIL_HOST_USER
            send_mail(subject,message,email_from,[em])
            return redirect(emailalert)
        else:
            return HttpResponse("failed to apply for the post")
    else:
        return render(request, 'userbook.html',{'an':an,'ds':ds,'rt':rt})

def emailalert(request):
    return render(request,'emailalert.html')

def wishlist(request,id):
    a=packageuploadmodel.objects.get(id=id)
    b=wishmodel(agency=a.agency,email=a.email,destina=a.destina,food=a.food,pet=a.pet,duration=a.duration,stay=a.stay,rate=a.rate)
    b.save()
    return redirect(wishdetail)


def wishdetail(request):
    a=wishmodel.objects.all()
    b=request.session['agency']
    return render(request,'wishlist.html',{'a':a,'b':b})

def removewish(request,id):
    b=wishmodel.objects.get(id=id)
    b.delete()
    return redirect(wishdetail)

def bookedusersdisplay(request):
    a=bookmodel.objects.all()
    c=request.session['agency']
    return render(request,'bookeduserlist.html',{'a':a,'c':c})

def confirmationmail(request,id):
    a = bookmodel.objects.get(id=id)
    email = a.email
    agency=a.agency

    if request.method == 'POST':
        c = confirmationemailform(request.POST)
        if c.is_valid():

            em = c.cleaned_data['email']
            me=a.cleaned_data['message']
            subject = f"{agency}"
            message = f"{me}"
            email_from = EMAIL_HOST_USER
            send_mail(subject, message, email_from, [em])
            return redirect(confirmationmail)
        else:
            return HttpResponse("failed to upload details")
    else:
        return render(request,'confirminput.html',{"a":email})

def confirmalert(request):
    return render(request,'confirmmail.html')

def agencyconfirm(request,id):
    b=bookmodel.objects.get(id=id)
    an=b.agency
    em=b.email
    if request.method=='POST':
        c=confirmationemailform(request.POST)
        if c.is_valid():
            an=c.cleaned_data['agency']
            em=c.cleaned_data['email']

            b=bookmodel(agency=an,email=em)
            b.save()
        # mail sending function
            subject=f"YOUR TOUR PACKAGE BOOKING IS CONFIRMED WITH {an} agency"
            message=f"hi, your package booking is confirmed .The agency team will contact you shortly."
            email_from = EMAIL_HOST_USER
            send_mail(subject,message,email_from,[em])
            return redirect(confirmalert)
        else:
            return HttpResponse("failed to confirm")
    else:
        return render(request, 'confirmmail.html',{'an':an})


def agencydetails(request):
    a=agencyregmodel.objects.all()
    return render(request,'agencydetails.html',{'a':a})

def userbio(request,id):
    a=userregmodel.objects.get(id=id)
    nm=a.name
    em=a.email
    ph=a.phone
    if request.method=='POST':
        a.name=request.POST.get('name')
        a.email=request.POST.get('email')
        a.phone=request.POST.get('phone')
        a.save()
        return redirect(displaybio)
    return render(request,'userbioprofile.html',{'a':a,'nm':nm,'em':em,'ph':ph})

def displaybio(request):
    a=userregmodel.objects.all()
    d=request.session['name']
    return render(request,'displaybio.html',{'a':a,'d':d})

def searchbox(request):
    a=placemodel.objects.all()
    if request.method=="POST":
        st=request.POST.get("searchstate")
        if st!=None:
            a=placemodel.objects.filter(state__icontains=st)
    return render(request,'states.html',{'a':a})