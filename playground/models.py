from django.db import models

# Create your models here.

class Collection(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name

class Cars(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.SET_NULL, null=True)
    
    creator = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=4)
    description = models.TextField(null=True, blank=True)
    pricePerDay = models.CharField(max_length=200)
    pricePerMonth = models.CharField(max_length=200)
    imageLink = models.CharField(max_length=1000)
    rentelStatus = models.BooleanField(default=False)


    def __str__(self):
        return self.creator + " " + self.name
    

class Custoumer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    mail = models.CharField(max_length=300)
    phone = models.CharField(max_length=200)
    location = models.CharField(max_length=500)
    licenesId = models.CharField(max_length=100)
    orderAt = models.DateField(auto_now_add=True)
    endDate = models.DateField(null=True)
    orderNote = models.CharField(max_length=500, null=True)
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.name 

