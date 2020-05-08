from django.contrib import admin
from .api.models import *
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['userid', 'fname', 'lname', 'email']

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = [ 'certificatenumber', 'id', 'reportnumber', 'userid', 'locationid', 'standardid', 'modelnumber'

    ]
    

@admin.register(ClientName)
class ClientNameAdmin(admin.ModelAdmin):
    list_display = [ 'clientid', 'clientname', 'clienttype'

    ]

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = [ 'locationid', 'address1', 'city', 'state', 'postalcode', 'phonenumber', 'clientid'

    ]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [ 'modelnumber', 'productname', 

    ]

@admin.register(TestStandard)
class TestStandardAdmin(admin.ModelAdmin):
    list_display = [ 'standardid', 'standardname', 'description'
        
    ]