from django.shortcuts import render, redirect
from hospital.models import Student,Staff,Other,Registered_Students
from django.contrib import messages
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db import IntegrityError
#import pillow


# Create your views here.

def register_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        DateofBirth = request.POST.get('DateofBirth')
        print(name,email,DateofBirth)
        Contact = request.POST.get('contact')
        Residence = request.POST.get('residence')
        gender = request.POST.get('gender')
        Weight = request.POST.get('Weight')
        Height = request.POST.get('Height')
        Marital_status = request.POST.get('Marital_status')
        current_medication = request.POST.get('current_medication')
        Next_of_kin = request.POST.get('Next_of_kin')
        Relationship = request.POST.get('Relationship')
        contact_Next_of_kin = request.POST.get('contact_Next_of_kin')
        reason_for_seeing_doctor = request.POST.get('reason_for_seeing_doctor')
        Registration_number = request.POST.get('Registration_number')
        Course = request.POST.get( "Course")
        consultation_fee = 5000
        
        if Registered_Students.objects.filter(Registration_number=Registration_number,name=name).exists():
            item = Registered_Students.objects.get(Registration_number=Registration_number)
            Amount_Paid = item.Amount_Paid
            #picture = item.picture
            Registered_Students.objects.filter(Registration_number= Registration_number).update(Amount_Paid = Amount_Paid-consultation_fee)
            student = Student.objects.create(name=name,email=email,DateofBirth=DateofBirth,Contact=Contact,Residence=Residence,gender=gender,Weight=Weight,Height=Height,Marital_status=Marital_status,current_medication=current_medication,Next_of_kin=Next_of_kin,Relationship=Relationship,contact_Next_of_kin=contact_Next_of_kin,reason_for_seeing_doctor=reason_for_seeing_doctor,Registration_number=Registration_number,Course=Course)
            student.save()
            messages.success(request,"Patient {} Saved Successfully".format(name))
        else:
            messages.error(request,"The entered student is not a Registered Student")
            return render(request,'registration.html')
        
        return render(request,'registration.html')
  
    return render(request,  'registration.html')

def register_staff(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        DateofBirth = request.POST.get('DateofBirth')
        print(name,email,DateofBirth)
        Contact = request.POST.get('contact')
        Residence = request.POST.get('residence')
        gender = request.POST.get('gender')
        Weight = request.POST.get('Weight')
        Height = request.POST.get('Height')
        Marital_status = request.POST.get('Marital_status')
        current_medication = request.POST.get('current_medication')
        Next_of_kin = request.POST.get('Next_of_kin')
        Relationship = request.POST.get('Relationship')
        contact_Next_of_kin = request.POST.get('contact_Next_of_kin')
        reason_for_seeing_doctor = request.POST.get('reason_for_seeing_doctor')
        
        staff = Staff.objects.create(name=name,email=email,DateofBirth=DateofBirth,Contact=Contact,Residence=Residence,gender=gender,Weight=Weight,Height=Height,Marital_status=Marital_status,current_medication=current_medication,Next_of_kin=Next_of_kin,Relationship=Relationship,contact_Next_of_kin=contact_Next_of_kin,reason_for_seeing_doctor=reason_for_seeing_doctor)
        staff.save()
        messages.success(request,"Patient {} Saved Successfully".format(name))
        return render(request,'registration.html')
  
    return render(request,  'registration.html')


def register_other(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        DateofBirth = request.POST.get('DateofBirth')
        print(name,email,DateofBirth)
        Contact = request.POST.get('contact')
        Residence = request.POST.get('residence')
        gender = request.POST.get('gender')
        Weight = request.POST.get('Weight')
        Height = request.POST.get('Height')
        Marital_status = request.POST.get('Marital_status')
        current_medication = request.POST.get('current_medication')
        Next_of_kin = request.POST.get('Next_of_kin')
        Relationship = request.POST.get('Relationship')
        contact_Next_of_kin = request.POST.get('contact_Next_of_kin')
        reason_for_seeing_doctor = request.POST.get('reason_for_seeing_doctor')
        
        other = Other.objects.create(name=name,email=email,DateofBirth=DateofBirth,Contact=Contact,Residence=Residence,gender=gender,Weight=Weight,Height=Height,Marital_status=Marital_status,current_medication=current_medication,Next_of_kin=Next_of_kin,Relationship=Relationship,contact_Next_of_kin=contact_Next_of_kin,reason_for_seeing_doctor=reason_for_seeing_doctor)
        other.save()
        messages.success(request,"Patient {} Saved Successfully".format(name))
        return render(request,'registration.html')
  
    return render(request,  'registration.html')
def doctor(request):
      student_data = serializers.serialize("python", Student.objects.all())
      staff_data = serializers.serialize("python", Staff.objects.all())
      other_data = serializers.serialize("python", Other.objects.all())
      
      number_of_other = Other.objects.count()
      number_of_student = Student.objects.count()
      number_of_Staff = Staff.objects.count()
      total_patients = number_of_Staff+number_of_other+number_of_student
      
      context = {'data':student_data,
                 'staff_data':staff_data,
                 'other_data':other_data,
                 'number_of_students': number_of_student,
                 'number_of_others' : number_of_other,
                 'number_of_Staff': number_of_Staff,
                 'total_patients':total_patients,
                 }
      
      
      return render(request, 'doctor.html',context = context)
  
def accounts(request):
    
    if request.method =="POST":
        name = request.POST['name']
        Registration_number = request.POST['Registration_number']
        Amount_Paid = request.POST['Amount_Paid']
        try:
            Registered_Students.objects.create(name=name,Registration_number=Registration_number,Amount_Paid=Amount_Paid)
            messages.success(request,"Student {} Saved Successfully".format(name))
        except IntegrityError:
            messages.error(request,"This Registration Number is already in use")
        except ValueError: 
            messages.error(request,"This Registration Number is already in use")
    return render(request, 'accounts.html')
       

# =============LOGIN FUNCTIONS ===========##
def logins(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        #print(username,password)
        user = authenticate(username=username,password=password)
        
        if user:
        
            super = User.objects.filter(username=username).get(is_superuser=True)
            if super:
                login(request,user)
                return redirect('doctor')
            elif User.groups.filter(username="receptionists").exists():
                return redirect('register')
        else:
            messages.error(request,"Error Bad Credentials")
            return render(request,'login.html')
            
    return render(request,'login.html')

def pharmacy(request):
    student_data = serializers.serialize("python", Student.objects.all())
    staff_data = serializers.serialize("python", Staff.objects.all())
    other_data = serializers.serialize("python", Other.objects.all())
      
    number_of_other = Other.objects.count()
    number_of_student = Student.objects.count()
    number_of_Staff = Staff.objects.count()
    total_patients = number_of_Staff+number_of_other+number_of_student
    
    context = {'data':student_data,
                'staff_data':staff_data,
                'other_data':other_data,
                'number_of_students': number_of_student,
                'number_of_others' : number_of_other,
                'number_of_Staff': number_of_Staff,
                'total_patients':total_patients
                }
    return render(request,'Pharmacy.html',context=context)

def login_reception(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        #print(username,password)
        user = authenticate(username=username,password=password)
        
        if user:
            login(request,user)
            return redirect('register')
        else:
            messages.error(request,"Error Bad Credentials")
            return render(request,'login.html')
            
    return render(request,'login.html')
def update_student_pharmacy(request):
    if request.method == 'POST':
        try:
            Registration_number  = request.POST.get('Registration_number')
            student = Student.objects.filter(Registration_number=Registration_number).exists()
            prescription = request.POST.get('prescription')
            
            if student:
                
                Student.objects.filter(Registration_number=Registration_number).update(prescription=prescription,)
                messages.success(request, "Patient with registration number {} has been updated successfully...".format(Registration_number))
        except ValueError:
                return messages.error(request,"The Registration Number You entered is Not Available \n Please check it and Try Again")    
    return redirect('pharmacy') 
    

def update_student(request):
    if request.method == 'POST':
        try:
            Registration_number  = request.POST.get('Registration_number')
            student = Student.objects.filter(Registration_number=Registration_number).exists()
            Desease = request.POST.get('Desease')
            Doctors_comment =request.POST.get('Doctors_comment')
            Medication_given = request.POST.get('Medication_given')
            lab_comment = request.POST.get('lab_comment')
            
            if student:
                
                Student.objects.filter(Registration_number=Registration_number).update(Desease=Desease, Doctors_comment=Doctors_comment,Medication_given=Medication_given,lab_comment=lab_comment)
                messages.success(request, "Patient with registration number {} has been updated successfully...".format(Registration_number))
        except ValueError:
                return messages.error(request,"The Registration Number You entered is Not Available \n Please check it and Try Again")    
    return redirect('doctor')  


def lab(request):
    if request.method == 'POST':
        try:
            Registration_number  = request.POST.get('Registration_number')
            student = Student.objects.filter(Registration_number=Registration_number).exists()
            lab_comment = request.POST.get('lab_comment')
            amount_charged = request.POST.get("amount_charged")
            if Registered_Students.objects.filter(Registration_number=Registration_number).exists():
                item = Registered_Students.objects.get(Registration_number=Registration_number)
                Amount_Paid = item.Amount_Paid
                Registered_Students.objects.filter(Registration_number= Registration_number).update(Amount_Paid = Amount_Paid- int(amount_charged))
            
            if student:
                
                Student.objects.filter(Registration_number=Registration_number).update(lab_comment=lab_comment)
                messages.success(request, "Patient with registration number {} has been updated successfully...".format(Registration_number))
        except ValueError:
                return messages.error(request,"The Registration Number You entered is Not Available \n Please check it and Try Again")    
    student_data = serializers.serialize("python", Student.objects.all())
    staff_data = serializers.serialize("python", Staff.objects.all())
    other_data = serializers.serialize("python", Other.objects.all())
      
    number_of_other = Other.objects.count()
    number_of_student = Student.objects.count()
    number_of_Staff = Staff.objects.count()
    total_patients = number_of_Staff+number_of_other+number_of_student
    
    context = {'data':student_data,
                'staff_data':staff_data,
                'other_data':other_data,
                'number_of_students': number_of_student,
                'number_of_others' : number_of_other,
                'number_of_Staff': number_of_Staff,
                'total_patients':total_patients
                }
      
    return render(request, "lab.html",context=context)     

def print_form(request):
    if request.method == "POST":
        Registration_number = request.POST.get('Registration_number')
        
        if Student.objects.filter(Registration_number=Registration_number).exists():
           medical_data = Student.objects.get(Registration_number=Registration_number)
           Registration_number = medical_data.Registration_number
           name = medical_data.name
           gender = medical_data.gender
           residence = medical_data.Residence
           date = medical_data.Date
           phone = medical_data.Contact
           Weight = medical_data.Weight
           Height = medical_data.Height
           Doctors_comment = medical_data.Doctors_comment
           lab_comment = medical_data.lab_comment
           Course = medical_data.Course
           prescription = medical_data.prescription
           Medication_given=medical_data.Medication_given
           patient_Id = medical_data.Unique_ID
           
           context = {
               'patient_Id':patient_Id, 
               'Registration_number': Registration_number,
                'name': name,
                'gender': gender,
                'residence': residence,
                'Date': date,
                'phone': phone,
                'Weight': Weight, 
                'Height': Height, 
                'Doctors_comment': Doctors_comment, 
                'lab_comment': lab_comment, 
                'Course': Course,
                'prescription': prescription,
                'Medication_given' :Medication_given,
           }
           print(context)
           return render(request,'med_form.html', context=context)
        else:
            messages.error(request,"The registration number you entered is not right pliz try again")   
    return render(request,'Pharmacy.html')    
        
        
            