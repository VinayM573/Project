from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager


UType = (
        ("User", "User"),
        ("Admin", "Admin"),
    )
ProcessName=(
        ("Finance","Finance"),
        ("Operation","Operation"),
        ("Associate","Associate"),
        ("IT","IT"),
        ("HR","HR")
)
Loaction=(
        ("Gurgoan","Gurgoan"),
        ("Noida","Noida")
    )

CATEGORY = (
    ("NMC", "NMC"),
    ("LFP", "LFP"),
    ("LCO", "LCO"),
)
CATEGORY1 = (
    ("EV", "EV"),
    ("Portable", "Portable"),
    ("Industrial", "Industrial"),
)
CATEGORY2 = (
    ("KG", "KG"),
    ("Gram", "Gram"),
    ("Unit", "Unit"),
)

CATEGORY3 = (
    ("BatX", "BatX"),
    ("Client", "Client"),
    ("Vinay", "Vinay"),
)
CATEGORY4 = (
    ("Regular", "Regular"),
    ("Contract", "Contract"),
)
CATEGORY5 = (
     ("Onboarding", "Onboarding"),
    ("Active", "Active"),
    ("Inactive", "Inactive"),
)   


class CustomUser(AbstractUser):
    username=None
    phone=models.CharField(max_length=10,unique=True)
    email=models.EmailField(max_length=100,unique=True,null=False)
    name=models.CharField(max_length=40)
    user_pic=models.ImageField(upload_to="user_pic",null=True)
    user_Type = models.CharField(max_length=40,choices=UType, null=True)
    department = models.CharField( max_length=40,choices=ProcessName,null=True)
    location = models.CharField(max_length=40,choices=Loaction,null=True)
    

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    objects=UserManager()
    
    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):
        if self.user_Type == 'Admin':
            self.is_staff=True
            self.is_active=True
            self.is_superuser = True
        elif self.user_Type == 'User':
            self.is_staff = False
            self.is_active = True
            self.is_superuser = False
        super().save(*args, **kwargs)


class ClientProfile(models.Model):
    cid =models.IntegerField(primary_key=True, auto_created=True)
    client_Name=models.CharField(max_length=40, null=True)
    business_Name=models.CharField(max_length=40, null=True)
    email = models.EmailField(max_length=40, null=True)
    contact=models.CharField(max_length=12, null=True)
    pan_Card=models.CharField(max_length=10, null=True)
    pan_Image=models.ImageField(upload_to="Pictures")
    aadhar_Card=models.CharField(max_length=12, null=True)
    adhar_Image=models.ImageField(upload_to="Pictures")
    address=models.CharField(max_length=40, null=True)
    assign_Person=models.CharField(max_length=40, null=True)
    industies_Type=models.CharField(max_length=20, choices=CATEGORY1, null=True)
    account_Type=models.CharField(max_length=20, choices=CATEGORY4, null=True)
    status=models.CharField(max_length=20, choices=CATEGORY5, null=True)

class Product(models.Model):
    product = models.CharField(max_length=40, null=True)
    Types_of_Cell = models.CharField(max_length=100, choices=CATEGORY, null=True)
    Industry_Type = models.CharField(max_length=20, choices=CATEGORY1, null=True)
    UOM = models.CharField(max_length=200,choices=CATEGORY2, null=True)
    price=models.PositiveIntegerField(null=True) 
    HSN_Code= models.PositiveIntegerField(null=True) 

    def __str__(self):
        return str(self.product)

class CRFQ(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    client = models.CharField(max_length=100, choices=CATEGORY3, null=True)
    rfqorder = models.CharField(max_length=100, null=True)
    rfqid = models.CharField(max_length=100, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    valid = models.DateTimeField(max_length=100, null=True)
    created_by = models.ForeignKey(CustomUser, models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)


