from django.urls import path, include
from front.views import views

from stale import views

urlpatterns = [

    path('', views.home, name='home'),
    path('staff/', views.staff, name='staff'),
    path('animals/', views.animals, name='animal'),
    path('species/', views.species, name='species'),

    # staff procedures
    path('staffedit/', views.createstaff, name='createstaff'),
    path(r'^updatestaff/<str:pk>/', views.updatestaff, name='updatestaff'),
    path(r'^deletestaff/<str:pk>/', views.deletestaff, name="deletestaff"),

    # Animal procedures
    path('createanimal/', views.createanimal, name='createanimal'),
    path(r'^updateanimal/<str:pk>/', views.updateanimal, name='updateanimal'),
    path(r'^deleteanimal/<str:pk>/', views.deleteanimal, name="deleteanimal"),

    # Species procedures
    path('createspecies/', views.createspecies, name='createspecies'),
    path(r'^updatespecies/<str:pk>/', views.updatespecies, name='updatespecies'),
    path(r'^deletespecies/<str:pk>/', views.deletespecies, name="deletespecies"),

    path('front/', include('front.urls')),

]

'''
1 - Submit email form                         //PasswordResetView.as_view()
2 - Email sent success message                //PasswordResetDoneView.as_view()
3 - Link to password Rest form in email       //PasswordResetConfirmView.as_view()
4 - Password successfully changed message     //PasswordResetCompleteView.as_view()
'''
