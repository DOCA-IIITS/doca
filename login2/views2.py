from django.core.mail import send_mail
from django.conf import settings

def send_otp(email_id,otp):

    subject = 'Your otp is '+str(otp)
    message = ' it  means a world to us thanks for choosing us \n your otp is : '+str(otp)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email_id,]

    send_mail( subject, message, email_from, recipient_list )

def send_otp2(email_id,otp):

    subject = 'Your otp to reset your password is '+str(otp)
    message = 'your otp is : '+str(otp)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email_id,]

    send_mail( subject, message, email_from, recipient_list )
