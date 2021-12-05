from django.shortcuts import render
from Ashtvinayak_Tank_Cleaner.forms import contactform
#to use email
from django.conf import settings 
from django.core.mail import send_mail 

# model
from .models import Image

#this is importing class 'conactformemail' from forms.py 
#from Ashtvinayak_Tank_Cleaner.forms import contactforemail

# Create your views here.

def index(request):
    portfolios = Image.objects.all()
    
    if request.method == "POST":
        
        #customer_name = request.POST['name']
        #customer_email = request.POST['email']
        #customer_subject = request.POST['subject']
        #customer_message = request.POST['message']
        #recipient_email = [settings.EMAIL_HOST_USER]
        #done = "Thank You "+ customer_name + ", we received your email and will respond shortly ! "
        #subject = "Customer: "+customer_name +" Subject: " +customer_subject + " Email: "+ customer_email
        #send_mail (
         #   subject,
         #   customer_message,
          #  customer_email,
           # ['thoratanil2008@gmail.com '],
        #)

        contact = contactform(request.POST) # here all data collected from form will send to from.py


        if contact.is_valid():
            customer_name = contact.cleaned_data['name']
            customer_email = contact.cleaned_data['email']
            customer_subject = contact.cleaned_data['subject']
            customer_message = contact.cleaned_data['message']
            recipient_email = [settings.EMAIL_HOST_USER]
            done = "Thank You "+ customer_name + ", we received your email and will respond shortly ! "
            subject = "Customer: "+customer_name +" Subject: " +customer_subject + " Email: "+ customer_email
            send_mail (
                subject,
                customer_message,
               customer_email,
              ['thoratanil2008@gmail.com '],
             )
            return render(request,'index.html',{'meassage':done}) 
    
    return render(request,'index.html',{'portfolios':portfolios,'media_url':settings.MEDIA_URL})  


def booking(request):
    if request.method == "POST":
        message_name = request.POST['name']
        message_email = request.POST['email']
        meassage_phone = request.POST['phone']
        message_date = request.POST['date']
        message_address = request.POST['address']
        
        done = "Thank You "+ message_name + ", our service will call you soon!"

        subject = "Customer: "+message_name +" Email: "+ message_email
        booking_details = "Customer: "+message_name+" requested booking at: "+message_address+" on "+message_date+". Phone no is :"+meassage_phone

        send_mail (
                subject,
                booking_details,
               message_email,
              ['thoratanil2008@gmail.com '],
             )

        return render(request,'booking.html',{'message':done})
    else:
        return render(request,'booking.html',{})
