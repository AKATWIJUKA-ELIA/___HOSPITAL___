from django.urls import path
from . import views

urlpatterns = [
    path('',views.register_student,name='register'),
    path('staff',views.register_staff,name='register_staff'),
    path('other',views.register_other,name='register_other'),
    path('doctor/',views.doctor,name='doctor'),
    path('accounts/',views.accounts,name='accounts'),
    path('login/', views.logins,name="login"),
    path('update_student/', views.update_student, name='update_student'),
    path('lab/', views.lab, name="lab"),
    path('pharmacy/', views.pharmacy, name='pharmacy'),
    path('update_student_pharmacy',views.update_student_pharmacy, name='update_student_pharmacy'),
    path('print',views.print_form,name= 'print_form')
]