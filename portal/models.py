from django.db import models

# Table to add tenant information
class rentdetails(models.Model):
    id= models.AutoField(primary_key=True)
    fname= models.CharField(max_length=50)
    lname= models.CharField(max_length=50)
    contact=models.CharField(max_length=13)
    email= models.CharField(max_length=20)
    laddress= models.CharField(max_length=80)
    pdetails= models.CharField(max_length=50)
    ramt= models.CharField(max_length= 6)
    damt= models.CharField(max_length=6)
    sdate= models.DateField()
    ldate= models.DateField()

    def __str__(self):
        return self.fname

#Table to save external user messages
class message(models.Model):
    id=models.AutoField(primary_key=True)
    mfname=models.CharField(max_length=15)
    mlname=models.CharField(max_length=15)
    mcontact=models.CharField(max_length=13)
    memail=models.CharField(max_length=25)
    mmessage=models.CharField(max_length=500)
    mdate=models.DateField()

    def __str__(self):
        return self.mfname
    


#Table to store payment details
class paymentdetails(models.Model):
    fname= models.CharField(max_length=50)
    lname= models.CharField(max_length=50)
    ramt= models.CharField(max_length=7)
    rmonth= models.CharField(max_length=10, null= True)
    rdate= models.DateField(null= True)
 
    def __str__(self):
        return self.fname 