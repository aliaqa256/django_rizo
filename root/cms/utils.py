import random
import string
from django.utils.text import slugify
import re
from . import jalali
from django.utils import timezone
from django.template.loader import render_to_string
from django.core.mail import send_mail
from cms import models 

'''
random_string_generator is located here:
http://joincfe.com/blog/random-string-generator-in-python/
'''


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


#print(random_string_generator())

#print(random_string_generator(size=50))


def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug



def restpassemail(email,domain):
    import uuid
    uuid=uuid.uuid4()
    pws=models.pwsrest(email = email, uuid= uuid)
    pws.save()
    message = render_to_string('account/email/rest_password.html', {
            'domain': domain,
            'uuid': uuid,
        })
    send_mail(
        'فراموشی پسورد ',
        message,
        domain,
        [email],
        fail_silently=False,
    )
    return True



def fixtimemin(mint):
    if mint > 55:
        return 60
    else :
        return mint+4 
        
####################################jalali###
###############################






def jcal(time):
    jmonths = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند",]

    time = timezone.localtime(time)

    time_to_str = "{},{},{}".format(time.year, time.month,time.day)
    time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()

    time_to_list = list(time_to_tuple)

    for index, month in enumerate(jmonths):
        if time_to_list[1] == index + 1:
            time_to_list[1] = month
            break

    output = "{} {} {}، ساعت {}:{}".format(
        time_to_list[2],
        time_to_list[1],
        time_to_list[0],
        time.hour,
        time.minute,
    )

    return output
##################shortlink

class Shortner:
    token_size=8
    def __init__(self,token_size=None):
        self.token_size = token_size if token_size is not None else 8

    def issue_token(self):
        letters=string.ascii_letters
        letters=letters+"0123456789"
        return ''.join(random.choice(letters) for i in range(self.token_size))   
