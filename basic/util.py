import string
import random

from django.core.mail import send_mail
from django.conf import settings

def otp_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def send_otp_email(email, otp):

    try: 
        message = "Your otp is %s" %(otp)
        email = send_mail('OTP for panorbit login', message, settings.EMAIL_HOST_USER, [email])
        #print(email)
    except Exception:
        return False
    
    return True
    
def validate_otp(otp, sent_otp, email, sent_email):
    if not sent_otp or not sent_email:
        result = {"success": False, "message": "session expired"}
        return result

    elif not email or not otp:
        result = {"success": False, "message": "didnot recieve proper data"}
        return result

    elif otp != sent_otp:
        result = {"success": False, "message": "wrong otp"}
        return result

    elif email != sent_email:
        result = {"success": False, "message": "wrong email"}
        return result

    else:    
        result = {"success": True, "message": "validated"}
        return result

