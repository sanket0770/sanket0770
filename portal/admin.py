import imp
from django.contrib import admin
from portal.models import rentdetails
from portal.models import paymentdetails
from portal.models import message

# Register your models here.
admin.site.register(rentdetails)
admin.site.register(paymentdetails)
admin.site.register(message)
