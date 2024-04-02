from django.db import models

class Student(models.Model):
    Unique_ID = models.AutoField(primary_key=True,)
    Date = models.DateTimeField(auto_now_add = True)
    name = models.CharField(max_length=255,default=0)
    DateofBirth = models.DateField(max_length = 255,default=None)
    Course = models.CharField(max_length=255)
    Registration_number = models.CharField(max_length = 255, unique=True, null=False,default=None)
    gender = models.CharField(max_length=6,default=None)
    Height = models.IntegerField(default=None)
    Weight = models.IntegerField(default=None)
    Next_of_kin = models.CharField(max_length = 255,default=None)
    contact_Next_of_kin = models.CharField(max_length = 13, blank=True,default=None)
    Relationship = models.CharField(max_length = 255,default=None)
    Marital_status = models.CharField(max_length = 25,default=None)
    Contact = models.CharField(max_length = 13, blank=True,default=None) #+91-xxxxxxxxx format
    email = models.EmailField(blank=True,default=None)
    Residence = models.CharField(max_length = 255,default=None)
    current_medication = models.CharField(max_length = 700,default=None,null = True)
    reason_for_seeing_doctor = models.CharField(max_length = 700,default=None)
    Desease = models.CharField(max_length = 500,default=None, null = True)
    Doctors_comment = models.CharField(max_length = 700,default=None, null = True)
    Medication_given = models.CharField(max_length = 500,default=None,null = True)
    
    
class Other(models.Model):
    Patient_Id = models.AutoField(primary_key = True)
    Date = models.DateTimeField(auto_now_add = True)
    name = models.CharField(max_length=20)
    DateofBirth = models.DateField()
    gender = models.CharField(max_length=6,default=None)
    Height = models.IntegerField()
    Weight = models.IntegerField()
    Next_of_kin = models.CharField(max_length = 255)
    Relationship = models.CharField(max_length = 255)
    contact_Next_of_kin = models.CharField(max_length = 13, blank=True)
    Marital_status = models.CharField(max_length = 25,default=None)
    Contact = models.CharField(max_length = 13, blank=True) #+91-xxxxxxxxx format
    email = models.EmailField(blank=True)
    Residence = models.CharField(max_length = 255)
    current_medication = models.CharField(max_length = 700,default=None)
    reason_for_seeing_doctor = models.CharField(max_length = 700,default=None)
    Desease = models.CharField(max_length = 500,default=None,null = True)
    Doctors_comment = models.CharField(max_length = 700,default=None,null = True)
    Medication_given = models.CharField(max_length = 500,default=None,null = True)
    
        
class Staff(models.Model):
    staff_Id = models.AutoField(primary_key = True)
    Date = models.DateTimeField(auto_now_add = True)
    name = models.CharField(max_length=20)
    DateofBirth = models.DateField()
    gender = models.CharField(max_length=6,default=None)
    Height = models.IntegerField()
    Weight = models.IntegerField()
    Next_of_kin = models.CharField(max_length = 255)
    Relationship = models.CharField(max_length = 255)
    contact_Next_of_kin = models.CharField(max_length = 13, blank=True)
    Marital_status = models.CharField(max_length = 25,default=None)
    Contact = models.CharField(max_length = 13, blank=True) #+91-xxxxxxxxx format
    email = models.EmailField(blank=True)
    Residence = models.CharField(max_length = 255)
    reason_for_seeing_doctor = models.CharField(max_length = 700,default=None)
    current_medication = models.CharField(max_length = 700,default=None)
    Desease = models.CharField(max_length = 500,default=None, null=True)
    Doctors_comment = models.CharField(max_length = 700,default=None,null=True)
    Medication_given = models.CharField(max_length = 500,default=None,null=True)
    
    
class Registered_Students(models.Model):
    def balance():
        pass
    name = models.CharField(max_length=225)
    Registration_number = models.CharField(max_length = 255, unique=True, null=False,primary_key =True)
    Amount_Paid = models.IntegerField(default=1220000)
    Balance = models.IntegerField(default=0,null=True)