# myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import CustomUser
from inventory.models import Product,CRFQ,ClientProfile,CustomUser

class CustomAuthenticationForm(AuthenticationForm):
    pass

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['user_Type','department', 'name','phone', 'email','location','user_pic','password1'] 
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_pic'].required = False


class ClientRegistry(forms.ModelForm):  
    class Meta:
        model = ClientProfile
        fields = [
            "client_Name",
            "business_Name",
            "email",
            "contact",
            "pan_Card",
            "pan_Image",
            "aadhar_Card",
            "adhar_Image",
            "address",
            "assign_Person",
            "industies_Type",
            "account_Type",
            "status",
        ]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["product","Types_of_Cell", "Industry_Type","UOM","price","HSN_Code"]

class CRFQForm(forms.ModelForm):
    class Meta:
        model = CRFQ
        fields = ["product","rfqid","rfqorder","order_quantity","client","valid"]

        
class ClientProfileForm(forms.ModelForm):
    class Meta:
        model = ClientProfile
        exclude = ['cid']
        fields = '__all__'

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email','user_Type','department', 'name','phone','location','user_pic']
        widgets = {
            'email': forms.EmailInput(attrs={'readonly': 'readonly'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_pic'].required = False

class ProfileImageForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=['user_pic']
