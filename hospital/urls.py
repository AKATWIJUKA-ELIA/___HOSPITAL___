from django.urls import path
from . import views

urlpatterns = [
    path('',views.register_student,name='register'),
    path('staff',views.register_staff,name='register_staff'),
    path('other',views.register_other,name='register_other'),
    path('doctor/',views.doctor,name='doctor'),
    path('accounts/',views.accounts,name='accounts'),
    path('login/', views.login,name="login"),
    path('update_student/', views.update_student, name='update_student')
    
]