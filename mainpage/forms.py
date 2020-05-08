from django import forms
from .api.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields ="__all__"
        labels = {
            "fname": "First Name",
            "lname": "Last Name",
            "mname": "Middle Name",
            "jobtitle": "Job Title",
            "email": "Email",
            "officephone": "Office Phone",
            "cellphone": "Cell Phone",
            "clientid": "Client ID"

        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = ClientName
        fields ="__all__"

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields ="__all__"
class TestSequenceForm(forms.ModelForm):
    class Meta:
        model = TestSequence
        fields ="__all__"
class PerformanceDataForm(forms.ModelForm):
    class Meta:
        model = PerformanceData
        fields ="__all__"
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields ="__all__"
class TestStandardForm(forms.ModelForm):
    class Meta:
        model = TestStandard
        fields ="__all__"
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields ="__all__"   
class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields ="__all__"   